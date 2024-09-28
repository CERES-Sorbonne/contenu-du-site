#!/bin/env bash
set +xe
# Liste les fichiers ajoutés lors du dernier commit
#new_files=$(git diff --find-renames --name-only --diff-filter=A -z HEAD~1)
IFS=$'\0'
new_files=()
while IFS= read -r -d $'\0'; do
  new_files+=("$REPLY")
done < <(git diff --find-renames --name-only --diff-filter=A -z HEAD~1)
unset IFS
echo "new_files: ${new_files[@]}"

for file in "${new_files[@]}"; do
  echo "file: $file"
done

for file in "${new_files[@]}"; do
  echo "Vérification du fichier: $file"
  # Vérifie si le fichier a un frontmatter (typique des fichiers Markdown)
  if [[ "$file" == *.md || "$file" == *.markdown ]]; then
    echo "Fichier Markdown détecté: $file"
    # Ajoute un UUID si le frontmatter n'en contient pas
    if ! grep -q 'uuid:' "$file"; then
      uuid=$(uuidgen)
      sed -i '0,/---/{s/---/---\nuuid: '"$uuid"'\n/}' "$file"
      echo "UUID ajouté au fichier: $file"
    fi
  fi
 done



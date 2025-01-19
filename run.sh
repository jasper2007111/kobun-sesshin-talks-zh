rm -rf ./root
mkdir root
mdbook build -d ./root
mdbook serve -d ./root

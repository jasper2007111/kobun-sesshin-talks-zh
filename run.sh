rm -rf ./public
mkdir public
mdbook build -d ./public
mdbook serve -d ./public

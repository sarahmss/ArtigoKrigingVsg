.PHONY: all clean fclean build 00_DotProduct  01_ExpSinesquared  02_RationalQuadratic  03_RBF  04_Matern  05_NoVirtualSamples 

# Diretórios contendo os notebooks 
DIRS = 00_DotProduct  01_ExpSinesquared  02_RationalQuadratic  03_RBF  04_Matern  05_NoVirtualSamples

# Executar todos os notebooks em todas as pastas
all: $(DIRS)

# Limpar todos os diretórios
clean: $(DIRS:%=clean-%)

# Limpar completamente todos os diretórios
fclean: $(DIRS:%=fclean-%)

# Construir todos os diretórios
build: $(DIRS:%=folders-%)

# Para cada diretório, executa os notebooks
$(DIRS):
	@echo "Executando notebooks no diretório $@"
	@cd $@ && $(MAKE) execute_notebooks

# Limpar cada diretório
$(DIRS:%=clean-%):
	@dir=$(@:clean-%=%) && echo "Limpando diretório $$dir" && cd $$dir && $(MAKE) clean

# Limpar completamente cada diretório
$(DIRS:%=fclean-%):
	@dir=$(@:fclean-%=%) && echo "Limpando completamente o diretório $$dir" && cd $$dir && $(MAKE) fclean

# Construir cada diretório
$(DIRS:%=folders-%):
	@dir=$(@:folders-%=%) && echo "Construindo o diretório $$dir" && cd $$dir && $(MAKE) folders

.PHONY: all folders clean fclean execute_notebooks

# Lista de notebooks
Notebooks =  Teste.ipynb Analizer.ipynb 

# Regra padrão que executa os notebooks
all: folders execute_notebooks

# Criar pastas necessárias
folders:
	mkdir -p ./results
	mkdir -p ./content
	mkdir -p ./content/models/
	mkdir -p ./content/models/initial-weights
	mkdir -p ./content/results/
	mkdir -p ./content/dataset/

# Limpeza completa
fclean:
	rm -rf ./content
	rm -rf ./results

# Limpeza parcial
clean:
	rm -rf ./content/models/*.keras
	rm -rf ./content/models/initial-weights/*.keras
	rm -rf ./content/results/*
	rm -rf ./content/dataset/*
	rm -rf ./results/*.xlsx

# Executar notebooks
execute_notebooks: $(Notebooks)
	@for notebook in $(Notebooks); do \
	  echo "Executando $$notebook..."; \
	  jupyter nbconvert --to notebook --execute "$$notebook" --inplace; \
	done

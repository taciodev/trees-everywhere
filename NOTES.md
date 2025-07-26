
# Observações do Modelo de Dados

- Uma conta poderá agrupar vários usuários e um usuário pode ser membro de várias contas. ✅

- O modelo User deverá ser uma extensão do modelo contrib.auth.models.User, com duas
funções que permitem plantar uma árvore em um local específico ou várias árvores de uma vez. ✅ 

- O local é definido por uma tupla com a latitude e longitude passadas como objetos Decimal. ✅ 

- Quando o método plant_tree for chamado, um objeto PlantedTrees deve ser criado e associado ao
usuário. ✅ 

- O método plant_trees permite registrar várias árvores de uma vez, passando uma lista de
tuplas em que o primeiro elemento é a árvore plantada e o segundo são as coordenadas. ✅ 

- Um usuário terá associado um objeto Profile, que pode conter um texto onde ele fala sobre si e a data em que ele entrou na plataforma. ✅ 

# Ideias de Melhorias

- TODO: Commitar as mudanças nas views e depois os repositories.
- TODO: Não deixar plantar em contas que o usuário não está cadastrado.
- TODO: Colocar na página de criação da conta no admin, uma forma de anexar usuário existentes naquele grupo.
- TODO: PlantedTree e PlantedTreeRepository. Verificar em qual app essas classes devem ficar.
- TODO: Mover o PlantedTreeRepository para o app users.

# Tarefas

1.

. Cadastro de novos usuários e senha. Deve permitir associar um usuário a uma conta. ✅ 
. Listagem e criação de contas (modelo Account). ✅ 
. Deve permitir ativar e desativar contas a partir da tela de listagem de contas. ✅ 
. Cadastro e visualização de plantas (modelo Plant). ✅ 
. A página de visualização de uma planta deve mostrar a lista de todas as plantas deste tipo que foram plantadas, incluindo o nome da pessoa que plantou. ✅

2. Criar template views para:

. Fazer login de um usuário que foi cadastrado pelo admin. ✅
. Visualizar as árvores plantadas por um usuário. ✅
. Um usuário não deverá poder visualizar as árvores plantadas por outro usuário
. Exibir os dados de uma árvore plantada selecionada.
. Adicionar uma árvore plantada.
. Exibir todas as árvores plantadas nas contas de que o usuário faz parte. ✅
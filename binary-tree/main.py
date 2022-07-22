class Vertice:
  def __init__(self, key, payload):
    self.key      = int(key)
    self.payload  = payload
    self.pai      = None
    self.left     = None
    self.right    = None

  def __str__(self):
    return "key: "+str(self.key)+" ==> "+"payload: "+str(self.payload)

class Tree:
  def __init__(self):
    self.raiz     = None
    self.count    = 0

  def tree_insert(self, z):
    y = None  #y começa apontando para o pai da raiz
    x = self.raiz #x é usado para detectar o vertice pai do adicionado

    while(x != None):
      y = x
      if(z.key < x.key):
        x = x.left
      else:
        x = x.right

    z.pai = y

    if(y == None):
      self.raiz = z
    elif(z.key < y.key):
      y.left = z
    else:
      y.right = z
    self.count += 1

  def interactive_tree_search(self, key):
    if(self.raiz == None):
      return None

    vertice = self.raiz

    while (vertice != None and int(key) != vertice.key):
      if(int(key) < vertice.key):
        vertice = vertice.left
      else:
        vertice = vertice.right

    return vertice
  
  def inorder_tree_walk(self, vertice = None):
    if (self.raiz == None): #árvore vazia
      return

    if (vertice == None): # por padrão começa na raíz
      vertice = self.raiz

    if (vertice.left != None):
      self.inorder_tree_walk(vertice = vertice.left)

    print(vertice)

    if (vertice.right != None):
      self.inorder_tree_walk(vertice = vertice.right)

  def tree_minimum(self, vertice = None):
    if (self.raiz == None):
      return

    if (vertice == None):
      vertice = self.raiz

    while (vertice.left != None):
      vertice = vertice.left

    return vertice
  
  def tree_successor(self, vertice):
    # Caso 1 - Possui a subárvore direita
    if (vertice.right != None):
      return self.tree_minimum(vertice = vertice.right)

    # Caso 2 - Não possui a subárvore direita
    y = vertice.pai
    while (y != None and vertice == y.right):
      vertice = y
      y = vertice.pai

    return y

  def tree_transplant(self, u, v):
    # caso 1
    if (u.pai == None):
      self.raiz = v
    elif (u.pai.left == u): # caso 2
      u.pai.left = v
    else:
      u.pai.right = v

    if (v != None):
      v.pai = u.pai # pai de u vira o pai de v em todos os casos
  
  '''
  A dificuldade dessa operação é encontrar um novo pai de família para 
  os filhos do vértice removido
  '''
  def tree_remove(self, z): # z --> vertice que vai ser removido
    if (z.left == None): # 1 caso
      '''
      Não possui a subárvore esquerda, então o filho direito será o novo
      pai da família de z que foi removido
      '''
      self.tree_transplant(z, z.right)
    
    elif (z.right == None): # 2 caso
      '''
      Não possui a subárvore direita, então o filho esquerdo será o novo
      pai da família de z que foi removido
      '''
      self.tree_transplant(z, z.left)
    else: # caso 3 - tem as duas subárvores
      y = self.tree_minimum(z.right) #encontra o vértice de menor chave na subárvore direita
      if(y.pai != z): # se y não for filho de z, tranplante a subárvore direita de y para a posição de y
        self.tree_transplant(y, y.right)
        y.right = z.right # Já ajusta os filhos direitos de y para ser a subárvore direita de z
        y.right.pai = y

      self.tree_transplant(z, y)
      y.left = z.left
      y.left.pai = y

  # -------------------- REPOSTAS DA SEGUNDA ATIVIDADE AVALIATIVA -------------------- #

  def tree_predecessor(self, vertice):
    if (vertice.left != None):
      return self.tree_maximum(vertice = vertice.left)

    y = vertice.pai
    while (y != None and vertice == y.left):
      vertice = y
      y = vertice.pai
    
    return y

  def tree_minimum_recursive(self, vertice = None):
    if (self.raiz == None):
      return

    if (vertice == None):
      vertice = self.raiz

    if (vertice.left != None):
      return self.tree_minimum_recursive(vertice = vertice.left)
    
    return vertice

  def tree_maximum(self, vertice=None):
    if (self.raiz == None):
      return

    if (vertice == None):
      vertice = self.raiz

    while (vertice.right != None):
      vertice = vertice.right

    return vertice
  
  def tree_print_decrescent(self, vertice = None):
    if (vertice == None):
      vertice = self.raiz

    if (vertice.right != None):
      self.tree_print_decrescent(vertice = vertice.right)

    print(vertice)

    if (vertice.left != None):
      self.tree_print_decrescent(vertice = vertice.left)
  
  def tree_pre_order(self, vertice = None):
    if (self.raiz == None):
      return

    '''
    primeiro raíz
    depois subárvore esquerda
    depois subárvore direita
    '''

    if (vertice == None):
      vertice = self.raiz
    
    print(vertice)
    
    if (vertice.left != None):
      self.tree_pre_order(vertice = vertice.left)

    if (vertice.right != None):
      self.tree_pre_order(vertice = vertice.right)
  
  def tree_pos_order(self, vertice=None):
    if (self.raiz == None):
      return
    
    '''
    primeiro subárvore esquerda
    depois subárvore direita
    depois raíz
    '''
    
    if (vertice == None):
      vertice = self.raiz

    if (vertice.left != None):
      self.tree_pos_order(vertice = vertice.left)

    if (vertice.right != None):
      self.tree_pos_order(vertice = vertice.right)
    
    print(vertice)
  
  def tree_remove_with_tree_maximum(self, z):
    print("z: ", z)
    if (z.left == None): # 1 caso
      self.tree_transplant(z, z.right)
    
    elif (z.right == None): # 2 caso
      self.tree_transplant(z, z.left)
    else: # 3 caso
      y = self.tree_maximum(z.left)
      if(y.pai != z): 
        self.tree_transplant(y, y.left)
        y.left = z.left 
        y.left.pai = y

      self.tree_transplant(z, y) 
      y.right = z.right
      y.right.pai = y


### --------------------------  MENU --------------------------  ###

tree = Tree()

while True:
  menu = [
    """
    1 - Inserir vertice na árvore
    2 - Listar todos os vertices da árvore
    3 - Pesquisar um vertice da árvore
    4 - Menor vertice da árvore
    5 - Pesquisar sucessor do vertice
    6 - Transplantar vertice
    7 - Remover vertice

    8 - Pesquisar predecessor do vertice
    9 - Menor vertice da árvore (recursivo)
    10 - Maior vertice da árvore
    11 - Listar de forma decrescente
    12 - Pre order
    13 - Post order
    14 - Remover vertice com tree_maximum
    15 - Sair do menu
    """
  ]

  print(menu[0])

  option = int(input("Digite uma opção: "))

  if (option == 1):
    key = int(input("Digite a chave: "))
    payload = input("Digite o payload: ")

    vertice = Vertice(key, payload)
    tree.tree_insert(vertice)

  elif (option == 2):
    print("")
    tree.inorder_tree_walk()

  elif (option == 3):
    key = int(input("Digite a chave de busca: "))
    vertice = tree.interactive_tree_search(key)
    print(vertice)

  elif (option == 4):
    min = tree.tree_minimum()
    print(min)

  elif (option == 5):
    key = int(input("Digite o vertice: "))
    vertice = tree.interactive_tree_search(key)

    successor = tree.tree_successor(vertice)
    print("O Sucessor do vertice %i é %s"%(key, successor))
  
  # elif (option == 6):
  #   u = int(input("Vertice que vai ser mudado: "))
  #   old_vertice = tree.interactive_tree_search(u)

  #   v = int(input("Vertice que vai ser colocado: "))
  #   vertice = Vertice(v, v)
  #   tree.tree_insert(vertice)

  #   new_vertice = tree.interactive_tree_search(v)

  #   tree.tree_transplant(old_vertice, new_vertice)
  #   print("Vertice mudado com sucesso!")

  elif (option == 7):
    z = int(input("Digite o vertice que vai ser deletado: "))
    vertice = tree.interactive_tree_search(z)

    tree.tree_remove(vertice)
    print("O vertice %i foi deletado com sucesso!"%(z))

  elif (option == 8):
    print("TREE PREDECESSOR")
    key = int(input("Digite o vertice: "))
    vertice = tree.interactive_tree_search(key)

    predecessor = tree.tree_predecessor(vertice)
    print("O Predecessor do vertice %i é %s"%(key, predecessor))

  elif (option == 9):
    print("TREE MINIMUM")
    min_rec = tree.tree_minimum_recursive()
    print(min_rec)

  elif (option == 10):
    print("TREE MAXIMUM")
    max = tree.tree_maximum()
    print(max)
  
  elif (option == 11):
    print("PRINT DECREMENT")
    tree.tree_print_decrescent()
  
  elif (option == 12):
    print("PRE ORDER")
    tree.tree_pre_order()
  
  elif (option == 13):
    print("POS ORDER")
    tree.tree_pos_order()
  
  elif (option == 14):
    print("TREE REMOVE")
    key = int(input("Digite o vertice que vai ser removido: "))
    vertice = tree.interactive_tree_search(key)
    print("vertice: ", vertice)

    tree.tree_remove_with_tree_maximum(vertice)

  elif (option == 15):
    break
  else:
    print("Opção inválida")
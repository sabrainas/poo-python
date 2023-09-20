from modulos import Casa, Pessoa

casa_da_ana = Casa()
ana = Pessoa('Ana')

ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(ana)

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar()
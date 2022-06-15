import pdb
from unittest import skip
from models.supplier import Supplier

import repositories.supplier_repository as supplier_repository

supplier_repository.delete_all()

supplier_1 = Supplier("Timber'R'Us", "T23952", "Peat Burns")
supplier_2 = Supplier("Rock Solid Concrete", "94337521RSC", "Saul Idd")
supplier_repository.save(supplier_1)
supplier_repository.save(supplier_2)

supplier_repository.select_all()

pdb.set_trace()

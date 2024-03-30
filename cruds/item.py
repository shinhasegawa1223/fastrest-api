from typing import Optional
from schemas import ItemCreate, ItemStatus, ItemUpdate


class Item:
    def __init__(
            self,
            id: int,
            name: str,
            price: int,
            description: Optional[str],
            status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status


items = [
    Item(1, "pc", 10000, "new", ItemStatus.ON_SALE),
    Item(2, "iPhone", 120000, "old", ItemStatus.SOLD_OUT),
    Item(3, "Xperia", 110000, "new", ItemStatus.ON_SALE),
]


def find_all():
    return items


def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None


def find_by_name(name: str):
    filtered_items = []
    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items


def create(item_create: ItemCreate):
    new_item = Item(
        len(items) + 1,
        item_create.name,
        item_create.price,
        item_create.description,
        ItemStatus.ON_SALE
    )
    items.append(new_item)
    return new_item


def update(id: int, item_update: ItemUpdate):
    print(item_update)
    print(id)
    for item in items:
        if item.id == id:
            print("if true")
            item.name = item_update.name if item_update.name is None else item_update.name
            item.status = item_update.description if item_update.description is None else item_update.description
            item.price = item_update.price if item_update.price is None else item_update.price
            item.status = item_update.status if item_update.status is None else item_update.status
            return item
    return None


def delete(id: int):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None

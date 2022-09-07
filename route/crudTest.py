from fastapi import APIRouter, status

crudTestRoute = APIRouter(prefix="/test", tags=["CRUD Template"])


@crudTestRoute.get("/{item}/{itemID}")
def get_Test(item: str, itemID: str):
    return {"message": f"Get {item}-{itemID} info"}


@crudTestRoute.post("/{item}", status_code=status.HTTP_201_CREATED)
def post_Test(item: str):
    return {"message": f"Create {item}"}


@crudTestRoute.put("/{item}/{itemID}")
def put_Test(item: str, itemID: int, changeID: int):
    return {"message": f"Update {item}-{itemID} to {item}-{changeID}"}


@crudTestRoute.delete("/{item}/{itemID}")
def delete_Test(item: str, itemID: int):
    return {"message": f"delete {item}-{itemID}"}


@crudTestRoute.get("/{item}")
def get_All_Test(item: str):
    return {"message": f"get all {item} infos"}

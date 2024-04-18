from routes.produto_routes import router as produto_router
from routes.setor_routes import router as setor_router
from routes.usuario_routes import router as usuario_router
from fastapi import FastAPI
app = FastAPI(title="Todos os problemas resolvidos, juntamente com o PUT",
              description="Problema de login resolvido, também foi resolvido o PUT do Setor que se encontrava em duplicidade no Header",
              )
@app.get('/health-check',tags=["PETHERSON HENRIQUE SILVA COSTA"])
def health_check():
    return True
app.include_router(setor_router)
app.include_router(produto_router)
app.include_router(usuario_router)


if __name__ == "__main__":
    import uvicorn
#                  #nomearquivo#nomeAppMain   
    uvicorn.run("main:app", host="127.0.0.1", port=8017, reload=True)
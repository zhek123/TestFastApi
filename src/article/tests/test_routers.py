async def test_list_articles(client):
    response = await client.get("/articles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


async def test_create_articles(client):
    articles_data = [
        {"title": "New Article", "description": "New Description"},
    ]
    response = await client.post("/articles/", json=articles_data)
    assert response.status_code == 201


async def test_get_article(client):
    articles_data = [
        {"title": "New Article", "description": "New Description"},
    ]
    await client.post("/articles/", json=articles_data)
    response = await client.get("/articles/")
    assert response.status_code == 200
    article_id = response.json()[0]["id"]
    response = await client.get(f"/articles/{article_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


async def test_update_articles(client):
    articles_data = [
        {"title": "New Article", "description": "New Description"},
    ]
    response = await client.post("/articles/", json=articles_data)
    assert response.status_code == 201
    article_id = response.json()[0]["id"]

    response = await client.patch(
        "/articles/",
        json={"title": "Updated Article", "description": "Updated " "Description", "article_ids": [article_id]},
    )
    assert response.status_code == 204


async def test_delete_articles(client):
    articles_data = [
        {"title": "New Article", "description": "New Description"},
    ]
    response = await client.post("/articles/", json=articles_data)
    assert response.status_code == 201
    article_id = response.json()[0]["id"]
    response = await client.delete_with_payload(url="/articles/", json=[article_id])

    assert response.status_code == 204

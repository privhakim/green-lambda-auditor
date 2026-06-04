from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def test_fast(self):
        self.client.get("/api/fast")

    @task(1)
    def test_heavy(self):
        self.client.get("/api/heavy")
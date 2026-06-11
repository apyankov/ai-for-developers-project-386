import type { Result, HealthResponse } from "@/types/generated";

const BASE = "/api/v1";

async function request<T>(path: string): Promise<Result<T>> {
  const res = await fetch(`${BASE}${path}`);
  return res.json() as Promise<Result<T>>;
}

export function getHealth(): Promise<Result<HealthResponse>> {
  return request<HealthResponse>("/health");
}

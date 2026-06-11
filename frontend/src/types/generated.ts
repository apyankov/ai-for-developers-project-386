export type HealthStatus = "ok" | "degraded";
export type DatabaseStatus = "connected" | "disconnected";

export interface HealthResponse {
  status: HealthStatus;
  version: string;
  database: DatabaseStatus;
  uptime: number;
}

export type Result<T> =
  | { type: "success"; data: T }
  | { type: "failure"; error: string; code: string };

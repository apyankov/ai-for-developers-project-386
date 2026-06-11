import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

import "./models/result.tsp";
import "./models/health.tsp";
import "./routes/health.tsp";

using TypeSpec.Http;
using TypeSpec.Rest;

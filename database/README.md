# Database assets

SQL files are grouped by purpose and named consistently by domain.

| Directory | Contents |
| --- | --- |
| [schema](schema/) | `buildings.sql`, `venues.sql`, and `events.sql`: the original ISA hierarchy definitions. |
| [seeds](seeds/) | Sample building, venue, and event records. |
| [queries](queries/) | Building, venue, and event query examples. |
| [security](security/) | `users.sql`: the original user table definition. |
| [examples/joins](examples/joins/) | Standalone join exercise: `schema.sql`, `data.sql`, and `queries.sql`. |

Schema diagrams and descriptions are in [docs/schema](../docs/schema/). Query execution screenshots are in [docs/evidence/queries](../docs/evidence/queries/).

The join exercise includes its own schema and dataset; treat it as a separate exercise rather than an additional migration for the main schema. The SQL assets are original coursework scripts, not an ordered migration system or a complete application bootstrap. Their statements and data are unchanged.

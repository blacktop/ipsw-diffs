## _CoreSpotlight_FoundationModels

> `/System/Library/Frameworks/_CoreSpotlight_FoundationModels.framework/Versions/A/_CoreSpotlight_FoundationModels`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x432d48
+2459.405.0.0.0
+  __TEXT.__text: 0x437a54
   __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0xac6a2
+  __TEXT.__const: 0xac6f2
   __TEXT.__constg_swiftt: 0xdf98
-  __TEXT.__swift5_typeref: 0x1185a
+  __TEXT.__swift5_typeref: 0x118aa
   __TEXT.__swift5_builtin: 0x7f8
-  __TEXT.__swift5_reflstr: 0x5407
-  __TEXT.__swift5_fieldmd: 0x1386c
+  __TEXT.__swift5_reflstr: 0x5437
+  __TEXT.__swift5_fieldmd: 0x1389c
   __TEXT.__swift5_assocty: 0x4990
   __TEXT.__swift5_proto: 0x6870
   __TEXT.__swift5_types: 0x1834
-  __TEXT.__cstring: 0x2a9a3
-  __TEXT.__swift5_capture: 0x2124
+  __TEXT.__cstring: 0x2c353
+  __TEXT.__swift5_capture: 0x212c
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0x508
   __TEXT.__swift_as_ret: 0x610
   __TEXT.__swift_as_cont: 0x4d4
   __TEXT.__swift5_mpenum: 0xbb8
   __TEXT.__oslogstring: 0x175
-  __TEXT.__unwind_info: 0x137c8
-  __TEXT.__eh_frame: 0x1a374
+  __TEXT.__unwind_info: 0x13828
+  __TEXT.__eh_frame: 0x1a424
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x870
+  __DATA_CONST.__objc_selrefs: 0x898
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x36d10
+  __AUTH_CONST.__const: 0x36dd8
   __AUTH_CONST.__objc_const: 0x1e80
-  __AUTH_CONST.__auth_got: 0x10e8
+  __AUTH_CONST.__auth_got: 0x1128
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x9d00
-  __DATA.__data: 0x11378
+  __DATA.__data: 0x11398
   __DATA.__bss: 0xcfbe0
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 28041
-  Symbols:   9347
-  CStrings:  2106
+  Functions: 28068
+  Symbols:   9357
+  CStrings:  2136
 
Symbols:
+ __swift_get_extra_inhabitant_index.135Tm
+ __swift_get_extra_inhabitant_index.91Tm
+ __swift_store_extra_inhabitant_index.136Tm
+ __swift_store_extra_inhabitant_index.92Tm
+ _objc_msgSend$bindVariable
+ _objc_msgSend$extractField
+ _objc_msgSend$fromStageId
+ _objc_msgSend$selector
+ _objc_msgSend$setTimeZone:
+ _swift_getObjCClassFromMetadata
+ _symbolic _____7content_SSSg5labelSS7stageIdt 31_CoreSpotlight_FoundationModels0B10SearchToolV0E5ReplyV7ContentO
+ _symbolic _____y_____7content_SSSg5labelSS7stageIdtG s23_ContiguousArrayStorageC 31_CoreSpotlight_FoundationModels0E10SearchToolV0H5ReplyV7ContentO
- __swift_get_extra_inhabitant_index.90Tm
- __swift_store_extra_inhabitant_index.91Tm
CStrings:
+ "\n\n**Temporal filters — pick the case by phrasing:**\n- \"in [year]\", \"in [Month year]\", \"on [date]\", \"during [period]\", \"today\", \"this week/month/year\" → **on** (a bounded period). \"in 2025\" → on(reference: absolute(year: 2025)). Auto-expands to the full period, so a bare year covers all of that year.\n- \"since [date]\", \"after [date]\", \"last [N] [units]\", \"recent\", \"past [N] days\" → **after**.\n- \"before [date]\", \"until [date]\", \"prior to [date]\" → **before**.\n- \"from [date] to [date]\", \"between [date] and [date]\" → **between**.\n- \"every [weekday/Month day/week N]\" (year-agnostic, repeating) → **recurring**. Use ONLY for genuinely recurring patterns, never for a specific year or date range.\n\nA specific year, month, or date is NOT recurring — use **on** (or **between** for a span). Only set temporal fields the user actually stated; set every field to a concrete value. Do NOT use variable-typed values in a root/filter predicate — variables are valid only when bound by an enclosing forEach stage."
+ "  Place names are often absent from the content and keyword text, so full-text (allText/keywords) alone can miss them — match the location fields. kMDItemNamedLocation is the primary location field: app-donated content (calendar events, reminders, and similar) stores the place's human-readable name there — typically a venue or place name — regardless of granularity, while kMDItemCity/kMDItemStateOrProvince/kMDItemFullyFormattedAddress are supplementary fields, present only on some file/photo items or when the token is a city, region, or street address. For ANY location token, always include kMDItemNamedLocation, and OR in kMDItemCity/kMDItemStateOrProvince/kMDItemFullyFormattedAddress as additional branches that match the token's shape. Never emit a location query that omits kMDItemNamedLocation. Recognize a place even when it reads like a topic or feature. For non-location attributes you're unsure of, prefer full-text (allText/semanticSimilar) over guessing an attribute name."
+ " To honor that ordering without dropping results, apply a temporal *ranking* model (recency/upcoming) via modelComposition — never a filter."
+ " declares .statistic in inputTypes but does not implement execute(statistic:value:)"
+ " result(s) are shown above. Do not search again — answer the user's question using those results."
+ "' (query stages are entry points and don't require an input)"
+ "' on query stage '"
+ "'. To find items of that content type, issue a search query with a contentType node instead."
+ "'. To find items, issue a search query instead of schema discovery."
+ "'. Valid schema-discovery types are: schema, attribute, content_type. To find items, do not use schema discovery — issue a search query instead."
+ "**First, decide whether a temporal filter belongs at all.** Add a temporal node only when the query names an explicit time — a date, month, year, or a phrase like \"today\", \"last week\", \"since June\", \"in 2025\". If the query names no time, add no temporal node: a filter *excludes* everything outside its window, and matching items may lie in the past as readily as the future. Words like \"upcoming\", \"recent\", or \"latest\" express ordering intent, not a time window — do not turn them into a filter."
+ "**JSON FORMAT for enum/union types:**\nAll enum types use discriminated union format: {\"type\": \"<caseName>\", \"value\": <payload>}\nExamples: {\"type\": \"search\", \"value\": {...}}, {\"type\": \"contentType\", \"value\": {\"contentTypes\": [...]}}\nPerson cases nest inside a person node: {\"type\": \"person\", \"value\": {\"type\": \"recipient\", \"value\": \"Alice Smith\"}}; self-relations inside personMe: {\"type\": \"personMe\", \"value\": {\"type\": \"fromMe\", \"value\": true}}\nAlways include the \"type\" key and \"value\" key."
+ "- Break down by / per / distribution (incl. per calendar period — per day/week/month/year) → groupBy + valueCount; for periods group by the derived period attribute, do NOT count date-range-filtered items"
+ "- Count/breakdown per period (\"how many … per month\", \"… by year\", \"weekly …\", \"distribution over time\") → groupBy the matching derived period attribute above + valueCount. This returns one count per bucket in a single stage. A date-range filter CANNOT do this — filtering yields raw items, not per-period counts, and hand-counting fetched items is wrong (it is capped by page size and misses buckets)."
+ "- Items within one period (\"notes from March\", \"emails last week\") → filter/query with a date-range predicate; no grouping."
+ "- Where something is → match the location fields, not full-text alone (place names are often missing from the content index, so allText/keywords can miss them): kMDItemNamedLocation is the primary field, holding the place's human-readable name (e.g. a venue) — always include it, then OR in kMDItemCity/kMDItemStateOrProvince/kMDItemFullyFormattedAddress as additional branches when the token also looks like a city, region, or street address. For other attributes you're unsure of, prefer full-text over guessing."
+ "- Which category/group has the most items → groupBy + valueCount(bindVariable) + filter"
+ "- Which most/least of an attribute (longest, highest-rated, newest) → sort by that attribute + limit"
+ "Ask yourself: does the question ask for a COUNT/BREAKDOWN *per* calendar period (per day/week/month/year), or for the ITEMS *within* one period?"
+ "Bound the range (e.g. a specific year) with a date predicate on the query stage, THEN group by the finer period attribute — never substitute the range filter for the grouping."
+ "Content type schema queries are not supported for '"
+ "Content type schema queries are not supported. To find items of a content type, issue a search query with a contentType node instead."
+ "ERROR: AgentPredicate: unparseable date string %{public}@ — date predicate will not match as intended."
+ "Input stage id. Omit on the entry-point query stage; set only when consuming a prior stage."
+ "Optional short display label for this stage's results."
+ "Schema query type 'attribute' requires an 'attribute' parameter naming the attribute to describe. To find items, issue a search query instead."
+ "Schema query type 'content_type' requires a 'contentType' parameter. To find items, issue a search query instead."
+ "Search query missing root predicate. Provide a root node (allText, contentType, predicate, or operation) describing what to match."
+ "SpotlightSearchTool: calling nativeTool.call (awaiting response)…"
+ "SpotlightSearchTool: nativeTool.call returned after %lds; yielding replies."
+ "SpotlightSearchTool: yielding output-node reply %d/%d status=%{public}@ stage=%{public}@."
+ "SpotlightSearchTool: yielding primary reply status=%{public}@ (%d output node(s) follow)."
+ "The first query stage reads the index directly — it has NO from. Only downstream stages carry from, naming a prior stage id."
+ "The tool argument did not match the FullArguments schema. The tool expects a JSON object whose `query` field is exactly one of:\n  {\"type\":\"search\", \"value\":<SearchArguments>}\n  {\"type\":\"schema\", \"value\":<SchemaQuery>}\n  {\"type\":\"help\",   \"value\":<HelpQuery>}\n  {\"type\":\"display\",\"value\":<DisplayQuery>}\n\nFor free-text search across all indexed text fields, retry with:\n  {\"query\":{\"type\":\"search\",\"value\":{\"root\":{\"type\":\"allText\",\"value\":{\"terms\":[\"<your terms>\"]}},\"pageSize\":15}}}\n\nDecode error: "
+ "This exact search already ran this turn; its "
+ "Unknown attribute '"
+ "Unknown schema query type '"
+ "handleSearchQuery(_:autoDisplay:modelFetchAttributes:)"
+ "kMDItemContentDescription"
+ "{id:\"q\", kind:query()} → {id:\"total\", output:agent, kind:count(from:\"q\")}"
+ "⚠️ NativeSpotlightSearchTool: stripped dangling from '"
+ "🔍     Stage %{public}@: %{public}@ bindVariable=%{public}@ extractValue.bindVariable=%{public}@"
+ "🔧 [post-mutation]     Stage %{public}@: %{public}@ bindVariable=%{public}@ extractValue.bindVariable=%{public}@"
+ "🔧 [post-mutation]   - pipeline stages: %{public}@"
- " declares .statistic in inputTypes but does not implement execute(statisticName:value:)"
- "**JSON FORMAT for enum/union types:**\nAll enum types use discriminated union format: {\"type\": \"<caseName>\", \"value\": <payload>}\nExamples: {\"type\": \"search\", \"value\": {...}}, {\"type\": \"contentType\", \"value\": {\"contentTypes\": [...]}}, {\"type\": \"recipient\", \"value\": \"Alice Smith\"}, {\"type\": \"fromMe\", \"value\": true}, {\"type\": \"agent\", \"value\": \"\"}\nAlways include the \"type\" key and \"value\" key."
- "- Break down by / per / distribution → groupBy + valueCount"
- "- Which most/least / peak → valueCount(bindVariable) + filter"
- "Content type schema queries not yet implemented via typed path"
- "Content type schema queries not yet implemented via typed path. Query type: "
- "Schema query type 'attribute' requires attribute parameter"
- "Schema query type 'content_type' requires contentType parameter"
- "Search query missing root predicate"
- "The tool argument did not match the FullArguments schema. The tool expects a JSON object whose `query` field is exactly one of:\n  {\"type\":\"search\", \"value\":<SearchArguments>}\n  {\"type\":\"schema\", \"value\":<SchemaQuery>}\n  {\"type\":\"help\",   \"value\":<HelpQuery>}\n  {\"type\":\"display\",\"value\":<DisplayQuery>}\n\nFor free-text search across all indexed text fields, retry with:\n  {\"query\":{\"type\":\"search\",\"value\":{\"root\":{\"type\":\"allText\",\"terms\":[\"<your terms>\"]},\"pageSize\":15}}}\n\nDecode error: "
- "Unknown schema query type: "
- "handleSearchQuery(_:autoDisplay:)"
- "{id:\"q\", kind:query(from:...)} → {id:\"total\", output:agent, kind:count(from:\"q\")}"
- "🔍     Stage %{public}@: %{public}@"
```

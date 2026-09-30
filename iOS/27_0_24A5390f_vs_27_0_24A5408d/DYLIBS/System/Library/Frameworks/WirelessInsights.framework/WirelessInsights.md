## WirelessInsights

> `/System/Library/Frameworks/WirelessInsights.framework/WirelessInsights`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-348.0.0.0.0
+350.1.0.0.0
   __TEXT.__text: 0x85480
   __TEXT.__objc_methlist: 0x5f0
   __TEXT.__gcc_except_tab: 0x4c04
CStrings:
+ "client:Got an unknown message from wirelessinsightsd!"
+ "client:xpc connection NULL while registering as component 0x%x"
+ "core:setExpectedMetricsForTrigger found %zd queryable metrics for trigger 0x%x"
+ "server.conn:No queryable callback for metric id 0x%x"
+ "server.conn:No queryable callback for metric id 0x%x for analytics"
- "client:Got an unkown message from wirelessinsightsd!"
- "client:xpc conenction NULL while registering as component 0x%x"
- "core:setExpectedMetricsForTrigger found %zd queriable metrics for trigger 0x%x"
- "server.conn:No queriable callback for metric id 0x%x"
- "server.conn:No queriable callback for metric id 0x%x for analytics"
```

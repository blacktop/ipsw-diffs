## trustd

> `/usr/libexec/trustd`

```diff

-61123.120.34.0.0
-  __TEXT.__text: 0x575b4
+61123.140.15.0.0
+  __TEXT.__text: 0x575bc
   __TEXT.__auth_stubs: 0x2270
   __TEXT.__objc_stubs: 0x25c0
   __TEXT.__objc_methlist: 0x798
   __TEXT.__const: 0x3695
   __TEXT.__gcc_except_tab: 0x7c8
   __TEXT.__cstring: 0x622a
-  __TEXT.__oslogstring: 0x4d65
+  __TEXT.__oslogstring: 0x4da2
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__objc_classname: 0x16d
   __TEXT.__objc_methname: 0x24a3
CStrings:
+ "%sev score: %ld %{private}@"
+ "%sev score: %ld lower than %ld %{private}@"
+ "completed: %{private}@ details: %{public}@ result: %d"
+ "found pinning %lu %@ policies for hostname %{private}@, policyName %{public}@"
+ "replacing %sev %s score: %ld with %sev score: %ld %{private}@"
- "%sev score: %ld %@"
- "%sev score: %ld lower than %ld %@"
- "completed: %@ details: %@ result: %d"
- "found pinning %lu %@ policies for hostname %@, policyName %@"
- "replacing %sev %s score: %ld with %sev score: %ld %@"

```

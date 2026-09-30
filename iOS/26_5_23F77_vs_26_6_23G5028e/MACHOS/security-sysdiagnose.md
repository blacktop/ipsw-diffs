## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61901.120.67.0.0
+61901.160.29.0.0
   __TEXT.__text: 0x3f70
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0xd0
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__gcc_except_tab: 0x188
   __TEXT.__objc_classname: 0x3d
   __TEXT.__objc_methname: 0x411
   __TEXT.__objc_methtype: 0x17e
-  __TEXT.__cstring: 0xeb3
+  __TEXT.__cstring: 0xe28
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0x100
   __DATA_CONST.__auth_got: 0x408

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 14027C84-1F48-32C5-91B9-4EE0CE5276C8
+  UUID: 34E1BBB5-B804-3F8C-B19C-3D44088B060B
   Functions: 34
   Symbols:   175
   CStrings:  308
CStrings:
+ "SELECT agrp,                                 SUM(1 - tomb) AS count_tomb_0,                                  SUM(tomb) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp                                  ORDER BY COUNT(*) DESC"
- "SELECT agrp,                                 SUM(CASE WHEN tomb = 0 THEN 1 ELSE 0 END) AS count_tomb_0,                                  SUM(CASE WHEN tomb = 1 THEN 1 ELSE 0 END) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp                                  ORDER BY (SUM(CASE WHEN tomb = 0 THEN 1 ELSE 0 END) + SUM(CASE WHEN tomb = 1 THEN 1 ELSE 0 END)) DESC"

```

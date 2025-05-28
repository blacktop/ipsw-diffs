## watchdogd

> `/usr/libexec/watchdogd`

```diff

-246.2.3.0.0
-  __TEXT.__text: 0x812c
+250.0.0.0.0
+  __TEXT.__text: 0x8098
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__objc_stubs: 0x620
-  __TEXT.__cstring: 0x35a2
+  __TEXT.__cstring: 0x34f8
   __TEXT.__const: 0x48
   __TEXT.__objc_classname: 0x1
   __TEXT.__oslogstring: 0x76

   - /usr/lib/libtailspin.dylib
   Functions: 188
   Symbols:   246
-  CStrings:  452
+  CStrings:  449
 
CStrings:
- "detected boot-arg (%s) to use customer service monitoring config"
- "monitoring for configd configured to panic on first timeout (see rdar://110674278)"
- "wdt_disable_110674278"

```

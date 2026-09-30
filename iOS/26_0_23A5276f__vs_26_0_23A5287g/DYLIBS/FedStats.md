## FedStats

> `/System/Library/PrivateFrameworks/FedStats.framework/FedStats`

```diff

-49.0.0.0.0
+52.0.0.0.0
   __TEXT.__text: 0x17e68
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x17a4

   __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x3380
-  __AUTH_CONST.__objc_const: 0x4de0
+  __AUTH_CONST.__objc_const: 0x3180
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xc30
   __DATA.__objc_ivar: 0x14c
-  __DATA.__data: 0x370
+  __DATA.__data: 0x360
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 861517C7-1B04-34D5-B85D-3D6B88F3FF69
+  UUID: D58C5836-B51E-3D48-8EB0-8D2A849F9831
   Functions: 437
-  Symbols:   1947
+  Symbols:   1897
   CStrings:  1575
 
Symbols:
- __WBSLocalizableStringsBundle
- __WBSLocalizableStringsBundleOnceToken
CStrings:
+ "\"%@\""
+ "INSERT INTO '%@' VALUES (%lu, \"%@\")"
+ "SELECT %@ FROM '%@' WHERE %@ == \"%@\" ORDER BY RANDOM() LIMIT 1"
+ "SELECT COUNT(1) AS %@ FROM '%@' WHERE %@ == \"%@\""
- "'%@'"
- "INSERT INTO '%@' VALUES (%lu, '%@')"
- "SELECT %@ FROM '%@' WHERE %@ == '%@' ORDER BY RANDOM() LIMIT 1"
- "SELECT COUNT(1) AS %@ FROM '%@' WHERE %@ == '%@'"

```

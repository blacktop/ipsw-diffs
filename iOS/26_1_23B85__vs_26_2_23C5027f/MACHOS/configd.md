## configd

> `/usr/libexec/configd`

```diff

-1385.40.9.0.0
-  __TEXT.__text: 0x67318
+1385.60.2.0.0
+  __TEXT.__text: 0x685ec
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x2f6d
-  __TEXT.__oslogstring: 0x5479
+  __TEXT.__cstring: 0x2fc1
+  __TEXT.__oslogstring: 0x55d6
   __TEXT.__objc_methname: 0x1a6b
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methtype: 0x501
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0xa18
   __DATA_CONST.__auth_got: 0x1280
   __DATA_CONST.__got: 0x6c0
   __DATA_CONST.__auth_ptr: 0x108

   __DATA.__objc_data: 0x190
   __DATA.__data: 0x104
   __DATA.__common: 0x80
-  __DATA.__bss: 0x648
+  __DATA.__bss: 0x640
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42127CA2-D2A1-3D57-9F70-7FEA9921F04A
-  Functions: 930
+  UUID: BB9F3209-11F2-3E5A-941A-1C1CAC44DDF4
+  Functions: 939
   Symbols:   820
-  CStrings:  1955
+  CStrings:  1969
 
CStrings:
+ "%@ missing/invalid %@"
+ "%@: %u reserved units, next built-in unit %u"
+ "%s: %@ has no specific unit"
+ "%s: %@ has reserved unit %@"
+ "%s: %@ has reserved unit %@, but it's not available"
+ "%s: %@ is ephemeral"
+ "Assigned %@ unit %@ (match known MAC address)"
+ "Assigned %@ unit %@ (match)"
+ "Assigned unit %@ (from database) to %@"
+ "Converting %@ to double failed"
+ "Converting %@ to int failed"
+ "Failed to assign unit %@ (%s) to %@"
+ "Failed to assign unit %@ to %@ using match %@"
+ "Invalid/missing int value %@"
+ "MatchingMACs before %@ after %@"
+ "Missing/invalid property %s in %@"
+ "Removed now active %@ from MatchingMACs"
+ "copyUnitForEstablishedInterface"
+ "interface_p != NULL && *interface_p != NULL"
+ "nameInterface"
+ "nameInterfacesAndCopyNameNeededList"
- "%@: has %u reserved units"
- "%s: %@ has reserved unit %u"
- "Interface assigned unit %@ (from database)"
- "Interface assigned unit %@ (updating database w/new interface)"
- "Interface assigned unit %@ (updating database w/previously used interface)"
- "assignNameAndCopyInterface"
- "nameInterfaces"

```

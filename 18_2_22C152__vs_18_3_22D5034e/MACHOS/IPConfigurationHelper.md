## IPConfigurationHelper

> `/System/Library/PrivateFrameworks/IPConfiguration.framework/XPCServices/IPConfigurationHelper.xpc/IPConfigurationHelper`

```diff

-494.60.3.0.0
-  __TEXT.__text: 0x6a4c
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_stubs: 0x620
+494.80.2.0.0
+  __TEXT.__text: 0x7420
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0xd0
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x29a
-  __TEXT.__objc_methname: 0x906
-  __TEXT.__oslogstring: 0x79f
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x23c
+  __TEXT.__objc_methname: 0x91b
+  __TEXT.__oslogstring: 0x81e
   __TEXT.__objc_classname: 0x9f
   __TEXT.__objc_methtype: 0x5a5
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x7e0
-  __DATA.__objc_selrefs: 0x1b8
+  __DATA.__objc_selrefs: 0x1c0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 39
-  Symbols:   125
-  CStrings:  236
+  Functions: 40
+  Symbols:   129
+  CStrings:  239
 
Symbols:
+ _CFArrayGetTypeID
+ _CFBooleanGetTypeID
+ _CFCopyTypeIDDescription
+ _CFDataGetTypeID
+ _CFDateGetTypeID
+ _CFDictionaryGetTypeID
+ _CFNumberGetTypeID
- _NSURLAuthenticationMethodServerTrust
- ___assert_rtn
- _objc_retain_x23
CStrings:
+ "%s: failed boundary checks at nesting level %d for elements array %@"
+ "RA PIO prefix '%@' found contained by PvD Additional Information prefix '%@'"
+ "allKeys"
+ "allValues"
+ "arrayWithObjects:count:"
+ "containsObject:"
+ "element is not a cfcollection: %@"
+ "element is not a cfprimitive: %@"
+ "enforce_proper_boundaries"
+ "expected '%@' element, got '%@'"
+ "expected String element, got '%@'"
+ "expected String or Dictionary element, got '%@'"
- "CFDictionaryGetCount(additionalInfoDict) == NECESSARY_FIELDS_COUNT"
- "IPHPvDInfoRequestServer.m"
- "RA PIO prefix '%@' found contained by PvDAdditional Information prefix '%@'"
- "authenticationMethod"
- "encountered a server authentication error, aborting fetch"
- "expected JSON Array of Strings"
- "expected JSON value of String type"
- "protectionSpace"
- "set_valid_necessary_fields"

```

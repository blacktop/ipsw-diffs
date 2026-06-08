## Diagnostic-4003

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4003.appex/Diagnostic-4003`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x1e4c
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x2f4
+1351.0.0.0.0
+  __TEXT.__text: 0x2030
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_methlist: 0x384
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__cstring: 0xaa
-  __TEXT.__objc_methname: 0x7cc
-  __TEXT.__oslogstring: 0x1ef
-  __TEXT.__objc_classname: 0x72
-  __TEXT.__objc_methtype: 0x239
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0x60
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__cstring: 0xce
+  __TEXT.__objc_methname: 0x923
+  __TEXT.__oslogstring: 0x214
+  __TEXT.__objc_classname: 0x9c
+  __TEXT.__objc_methtype: 0x27e
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x100
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x4a0
-  __DATA.__objc_selrefs: 0x278
-  __DATA.__objc_ivar: 0x28
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x78
+  __DATA.__objc_const: 0x5f0
+  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x180
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 190445F9-87B3-3513-AFE1-A7BF859C26D8
-  Functions: 51
-  Symbols:   85
-  CStrings:  177
+  UUID: 31025746-64CD-3FC0-9FFF-6E2E7E987931
+  Functions: 59
+  Symbols:   104
+  CStrings:  200
 
Symbols:
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFStringGetTypeID
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryCreateIterator
+ _IORegistryEntryCreateCFProperty
+ _OBJC_CLASS_$_AmbientLightSensorDataInputs
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ _OBJC_METACLASS_$_AmbientLightSensorDataInputs
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kIOMainPortDefault
+ _objc_alloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
- _objc_release_x24
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"NSDictionary\""
+ "AmbientLightSensorDataInputs"
+ "B24@0:8@\"NSDictionary\"16"
+ "B32@0:8@16@24"
+ "B32@0:8@16Q24"
+ "Could not create IORegistry iterator"
+ "DKDiagnosticInputs"
+ "IOService"
+ "LocationID"
+ "Product"
+ "T@\"NSDictionary\",&,N,V_additionalMatching"
+ "_additionalMatching"
+ "additionalMatching"
+ "dictionary"
+ "initWithData:encoding:"
+ "isEqualToString:"
+ "resolveMatchingForProduct:hidEvent:"
+ "setAdditionalMatching:"
+ "startMonitoringWithHIDEvents:additionalMatching:"
+ "validateAndInitializeParameters:"
+ "validateAndInitializePredicates:"
+ "validateAndInitializeSpecifications:"
- "\""

```

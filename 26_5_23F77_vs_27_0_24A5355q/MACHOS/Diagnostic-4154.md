## Diagnostic-4154

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4154.appex/Diagnostic-4154`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x85d8
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0x2280
-  __TEXT.__objc_methlist: 0xa3c
+1351.0.0.0.0
+  __TEXT.__text: 0x7c08
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x22e0
+  __TEXT.__objc_methlist: 0xa6c
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x329
-  __TEXT.__objc_classname: 0xbd
-  __TEXT.__objc_methname: 0x2587
-  __TEXT.__objc_methtype: 0x329
-  __TEXT.__oslogstring: 0x17e
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x130
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__cstring: 0x354
+  __TEXT.__objc_classname: 0xb0
+  __TEXT.__objc_methname: 0x265b
+  __TEXT.__objc_methtype: 0x345
+  __TEXT.__oslogstring: 0x1a3
+  __TEXT.__unwind_info: 0x1a8
   __DATA_CONST.__const: 0x108
-  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x50
   __DATA_CONST.__objc_intobj: 0x2a0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x11e8
-  __DATA.__objc_selrefs: 0x9e0
-  __DATA.__objc_ivar: 0x120
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x138
+  __DATA.__objc_const: 0x1218
+  __DATA.__objc_selrefs: 0xa08
+  __DATA.__objc_ivar: 0x124
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
   __DATA.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A738E17D-9711-3C15-9F6C-29FC909EDD19
-  Functions: 204
-  Symbols:   146
-  CStrings:  643
+  UUID: 01B94B64-48D0-3345-AA44-211B9E36E895
+  Functions: 209
+  Symbols:   161
+  CStrings:  657
 
Symbols:
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFStringGetTypeID
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryCreateIterator
+ _IORegistryEntryCreateCFProperty
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kIOMainPortDefault
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "B32@0:8@16@24"
+ "B32@0:8@16Q24"
+ "Could not create IORegistry iterator"
+ "IOService"
+ "LocationID"
+ "Product"
+ "T@\"NSDictionary\",&,N,V_additionalMatching"
+ "_additionalMatching"
+ "additionalMatching"
+ "initWithData:encoding:"
+ "resolveMatchingForProduct:hidEvent:"
+ "setAdditionalMatching:"
+ "startMonitoringWithHIDEvents:additionalMatching:"
- "\""

```

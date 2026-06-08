## Diagnostic-4006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4006.appex/Diagnostic-4006`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x1998
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x28c
+1351.0.0.0.0
+  __TEXT.__text: 0x1c70
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x92
-  __TEXT.__oslogstring: 0x149
-  __TEXT.__objc_classname: 0x55
-  __TEXT.__objc_methname: 0x62f
-  __TEXT.__objc_methtype: 0x1e6
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0xb4
+  __TEXT.__oslogstring: 0x16e
+  __TEXT.__objc_classname: 0x51
+  __TEXT.__objc_methname: 0x71f
+  __TEXT.__objc_methtype: 0x212
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0xe0
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x168
-  __DATA.__objc_const: 0x3f0
-  __DATA.__objc_selrefs: 0x228
-  __DATA.__objc_ivar: 0x1c
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x70
+  __DATA.__objc_const: 0x420
+  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4FD74F1-17E6-321A-9B4C-301EBE1B059C
-  Functions: 44
-  Symbols:   82
-  CStrings:  150
+  UUID: 348E292A-F5A2-3DB0-80C0-36178DA1F55D
+  Functions: 49
+  Symbols:   99
+  CStrings:  167
 
Symbols:
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFStringGetTypeID
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryCreateIterator
+ _IORegistryEntryCreateCFProperty
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kIOMainPortDefault
+ _objc_alloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
- _objc_release_x24
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"NSDictionary\""
+ "B32@0:8@16@24"
+ "B32@0:8@16Q24"
+ "Could not create IORegistry iterator"
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
- "\""

```

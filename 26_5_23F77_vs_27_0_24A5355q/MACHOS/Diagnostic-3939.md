## Diagnostic-3939

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x81dc
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xa7c
+1351.0.0.0.0
+  __TEXT.__text: 0x7a40
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x19a0
+  __TEXT.__objc_methlist: 0xaac
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__cstring: 0x32c
-  __TEXT.__objc_methname: 0x1e47
-  __TEXT.__oslogstring: 0x42a
-  __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0x58e
-  __TEXT.__unwind_info: 0x328
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x128
+  __TEXT.__gcc_except_tab: 0x2ec
+  __TEXT.__cstring: 0x359
+  __TEXT.__objc_methname: 0x1f39
+  __TEXT.__oslogstring: 0x44f
+  __TEXT.__objc_classname: 0x19f
+  __TEXT.__objc_methtype: 0x5aa
+  __TEXT.__unwind_info: 0x258
   __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__objc_doubleobj: 0x70
-  __DATA.__objc_const: 0x16d0
-  __DATA.__objc_selrefs: 0x848
-  __DATA.__objc_ivar: 0xdc
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x140
+  __DATA.__objc_const: 0x1700
+  __DATA.__objc_selrefs: 0x878
+  __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EE50309D-CA1D-378B-9DCA-1A7A4E3E5220
-  Functions: 230
-  Symbols:   182
-  CStrings:  639
+  UUID: 20554FB4-7C24-38FB-8593-A7173D13951A
+  Functions: 233
+  Symbols:   196
+  CStrings:  655
 
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
+ _OBJC_CLASS_$_UITraitCollection
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kIOMainPortDefault
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x4
+ _objc_retain_x8
- _OBJC_CLASS_$_UIScreen
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
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
+ "currentTraitCollection"
+ "dictionary"
+ "displayScale"
+ "initWithData:encoding:"
+ "resolveMatchingForProduct:hidEvent:"
+ "setAdditionalMatching:"
+ "startMonitoringWithHIDEvents:additionalMatching:"
- "mainScreen"
- "scale"

```

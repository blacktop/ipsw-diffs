## Diagnostic-4276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4276.appex/Diagnostic-4276`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x5d44
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x95c
-  __TEXT.__cstring: 0x318
-  __TEXT.__objc_methname: 0x18af
-  __TEXT.__objc_classname: 0xfd
-  __TEXT.__objc_methtype: 0x4f4
+1351.0.0.0.0
+  __TEXT.__text: 0x5994
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_stubs: 0x1760
+  __TEXT.__objc_methlist: 0x98c
+  __TEXT.__cstring: 0x346
+  __TEXT.__objc_methname: 0x198e
+  __TEXT.__objc_classname: 0xed
+  __TEXT.__objc_methtype: 0x520
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__oslogstring: 0x2fe
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__gcc_except_tab: 0x110
+  __TEXT.__oslogstring: 0x323
+  __TEXT.__unwind_info: 0x230
   __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x70
-  __DATA.__objc_const: 0xec8
-  __DATA.__objc_selrefs: 0x750
-  __DATA.__objc_ivar: 0xa4
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x108
+  __DATA.__objc_const: 0xef8
+  __DATA.__objc_selrefs: 0x780
+  __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x180
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 089B8962-4867-3CC6-9C7B-EE4C82D7A4E2
-  Functions: 202
-  Symbols:   150
-  CStrings:  499
+  UUID: DAE4D39E-7468-32D4-BFD1-BF30DD413147
+  Functions: 204
+  Symbols:   166
+  CStrings:  515
 
Symbols:
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFStringGetTypeID
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryCreateIterator
+ _IORegistryEntryCreateCFProperty
+ _OBJC_CLASS_$_NSString
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kIOMainPortDefault
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
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
+ "resolveMatchingForProduct:hidEvent:"
+ "setAdditionalMatching:"
+ "startMonitoringWithHIDEvents:additionalMatching:"
- "\""

```

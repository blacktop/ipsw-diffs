## libAmber.dylib

> `/usr/lib/libAmber.dylib`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0xb4928
+30.0.0.0.0
+  __TEXT.__text: 0xb4d10
   __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x20c
-  __TEXT.__gcc_except_tab: 0x9c04
-  __TEXT.__cstring: 0x10f02
+  __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__gcc_except_tab: 0x9c54
+  __TEXT.__cstring: 0x10ff4
   __TEXT.__const: 0x1d96
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x39c8
-  __TEXT.__objc_classname: 0x85
-  __TEXT.__objc_methname: 0x6f7
-  __TEXT.__objc_methtype: 0x1c8
+  __TEXT.__unwind_info: 0x39e0
+  __TEXT.__objc_classname: 0xa0
+  __TEXT.__objc_methname: 0x818
+  __TEXT.__objc_methtype: 0x253
   __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__const: 0x40e8
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x470
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__objc_const: 0x570
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x20
   __DATA.__data: 0xc0
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FDD33DCD-D8CC-3313-8BE9-67FEC524EF4A
-  Functions: 2313
-  Symbols:   6569
-  CStrings:  2831
+  UUID: 64C4603F-5D1E-3828-86B1-2C4368836F07
+  Functions: 2330
+  Symbols:   6614
+  CStrings:  2861
 
Symbols:
+ -[AmberDylibNSURLInputStream _scheduleInCFRunLoop:forMode:]
+ -[AmberDylibNSURLInputStream _setCFClientFlags:callback:context:]
+ -[AmberDylibNSURLInputStream _unscheduleFromCFRunLoop:forMode:]
+ -[AmberDylibNSURLInputStream amberRequest]
+ -[AmberDylibNSURLInputStream close]
+ -[AmberDylibNSURLInputStream getBuffer:length:]
+ -[AmberDylibNSURLInputStream hasBytesAvailable]
+ -[AmberDylibNSURLInputStream initWithAmberRequest:]
+ -[AmberDylibNSURLInputStream open]
+ -[AmberDylibNSURLInputStream propertyForKey:]
+ -[AmberDylibNSURLInputStream read:maxLength:]
+ -[AmberDylibNSURLInputStream removeFromRunLoop:forMode:]
+ -[AmberDylibNSURLInputStream setProperty:forKey:]
+ -[AmberDylibNSURLInputStream setStatus:]
+ -[AmberDylibNSURLInputStream status]
+ -[AmberDylibNSURLInputStream streamStatus]
+ _OBJC_CLASS_$_AmberDylibNSURLInputStream
+ _OBJC_CLASS_$_NSInputStream
+ _OBJC_IVAR_$_AmberDylibNSURLInputStream._amberRequest
+ _OBJC_IVAR_$_AmberDylibNSURLInputStream._status
+ _OBJC_METACLASS_$_AmberDylibNSURLInputStream
+ _OBJC_METACLASS_$_NSInputStream
+ __OBJC_$_INSTANCE_METHODS_AmberDylibNSURLInputStream
+ __OBJC_$_INSTANCE_VARIABLES_AmberDylibNSURLInputStream
+ __OBJC_$_PROP_LIST_AmberDylibNSURLInputStream
+ __OBJC_CLASS_RO_$_AmberDylibNSURLInputStream
+ __OBJC_METACLASS_RO_$_AmberDylibNSURLInputStream
+ __ZN5amber16NSURLHTTPRequest13readInputDataEPhm
+ __ZN5amber20DiskImagePluginImage12copy_uuid_cbEP18_di_plugin_image_t
+ __ZN5amber23DiskImagePluginNBDImage8copyUUIDEv
+ __ZN5amber24DiskImagePluginKnoxImage8copyUUIDEv
+ __ZN5amber29DiskImagePluginAmberKnoxImage8copyUUIDEv
+ _objc_msgSend$initWithAmberRequest:
+ _objc_msgSend$setHTTPBodyStream:
- _OBJC_CLASS_$_NSData
- __ZN5amber20DiskImagePluginImage11get_uuid_cbEP18_di_plugin_image_t
- __ZN5amber23DiskImagePluginNBDImage4uuidEv
- __ZN5amber24DiskImagePluginKnoxImage4uuidEv
- __ZN5amber29DiskImagePluginAmberKnoxImage4uuidEv
- _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
- _objc_msgSend$setHTTPBody:
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/Amber/Amber/Source/HTTP/.././Memory/./MemoryOperations.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/Amber/Amber/Source/HTTP/.././Memory/./MutableMemoryView.hpp"
+ "30"
+ "@24@0:8@16"
+ "AmberDylibNSURLInputStream"
+ "B32@0:8@16@24"
+ "B32@0:8^*16^Q24"
+ "Content-Length header"
+ "Content-Length: %zu"
+ "Q"
+ "TQ,N,V_status"
+ "T^v,R,N,V_amberRequest"
+ "_scheduleInCFRunLoop:forMode:"
+ "_setCFClientFlags:callback:context:"
+ "_status"
+ "_unscheduleFromCFRunLoop:forMode:"
+ "getBuffer:length:"
+ "hasBytesAvailable"
+ "initWithAmberRequest:"
+ "invalid attribute data"
+ "propertyForKey:"
+ "q32@0:8*16Q24"
+ "read:maxLength:"
+ "removeFromRunLoop:forMode:"
+ "setHTTPBodyStream:"
+ "setProperty:forKey:"
+ "setStatus:"
+ "streamStatus"
+ "v24@0:8Q16"
+ "v32@0:8^{__CFRunLoop=}16^{__CFString=}24"
+ "v72@0:8Q16^?24{?=q^v^?^?^?}32"
- "29"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "invalid attribute"
- "setHTTPBody:"

```

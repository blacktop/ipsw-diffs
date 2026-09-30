## seserviced

> `/usr/libexec/seserviced`

```diff

-51.5.1.0.0
-  __TEXT.__text: 0x3579ac
-  __TEXT.__auth_stubs: 0x3a10
-  __TEXT.__objc_stubs: 0x8ba0
-  __TEXT.__objc_methlist: 0x40f0
-  __TEXT.__const: 0x93a0
+51.8.0.0.0
+  __TEXT.__text: 0x357e30
+  __TEXT.__auth_stubs: 0x3990
+  __TEXT.__objc_stubs: 0x8bc0
+  __TEXT.__objc_methlist: 0x4110
+  __TEXT.__const: 0x9380
   __TEXT.__gcc_except_tab: 0x29dc
-  __TEXT.__objc_methname: 0x11d68
-  __TEXT.__oslogstring: 0x151af
-  __TEXT.__cstring: 0x2c40b
-  __TEXT.__objc_classname: 0x116c
-  __TEXT.__objc_methtype: 0x603a
+  __TEXT.__objc_methname: 0x11df2
+  __TEXT.__oslogstring: 0x151bf
+  __TEXT.__cstring: 0x2c3de
+  __TEXT.__objc_classname: 0x118c
+  __TEXT.__objc_methtype: 0x6070
   __TEXT.__swift5_typeref: 0x3a9c
   __TEXT.__constg_swiftt: 0x3c98
   __TEXT.__swift5_reflstr: 0x3eea

   __TEXT.__swift5_types: 0x41c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__unwind_info: 0x84d0
-  __TEXT.__eh_frame: 0xfea4
-  __DATA_CONST.__auth_got: 0x1d18
-  __DATA_CONST.__got: 0xfc0
-  __DATA_CONST.__auth_ptr: 0xba8
-  __DATA_CONST.__const: 0xf0f0
-  __DATA_CONST.__cfstring: 0x11a80
+  __TEXT.__unwind_info: 0x84e0
+  __TEXT.__eh_frame: 0xfe58
+  __DATA_CONST.__auth_got: 0x1cd8
+  __DATA_CONST.__got: 0xfb8
+  __DATA_CONST.__auth_ptr: 0xb18
+  __DATA_CONST.__const: 0xf118
+  __DATA_CONST.__cfstring: 0x11b00
   __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x400
+  __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x240

   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x8d0
-  __DATA.__objc_const: 0x183e0
-  __DATA.__objc_selrefs: 0x36c8
-  __DATA.__objc_ivar: 0xbf0
+  __DATA.__objc_const: 0x184a8
+  __DATA.__objc_selrefs: 0x36d8
+  __DATA.__objc_ivar: 0xbfc
   __DATA.__objc_data: 0x6150
-  __DATA.__data: 0xa018
-  __DATA.__bss: 0xb8c0
+  __DATA.__data: 0xa078
+  __DATA.__bss: 0xb898
   __DATA.__common: 0x58a
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10116
-  Symbols:   1602
-  CStrings:  9901
+  Functions: 10117
+  Symbols:   1594
+  CStrings:  9904
 
Symbols:
- __availability_version_check
- _fseek
- _swift_taskGroup_wait_next_throwing
- _dispatch_once_f
- _sscanf
- _fclose
- _fread
- _rewind
CStrings:
+ "-[KmlEndpointManager upgradeVersionType:version:upgradeInformation:]_block_invoke"
+ "_upgradeInfoData"
+ "@\"<KmlEndpointManagerDelegate>\""
+ "\x17"
+ "\x0e\x13"
+ "Missing certificates"
+ "Waiting for upgrade to finish"
+ "_upgradeCompletionCallback"
+ "@\"KmlEndpointManager\""
+ "\xf01"
+ "unlockSource"
+ "rangingExceptionBitmap"
+ "-[KmlKeyManagementSession handleUpgradeCompletionWithStatus:]"
+ "Missing Instance CA certificate"
+ "_epManager"
+ "KmlEndpointManagerDelegate"
+ "handleUpgradeCompletionWithStatus:"
+ "iOS (18.1) - SecureElementService-51.8"
+ "%!@(MISSING) - %!@(MISSING)"
+ "-[KmlEndpointManager convertEndpoint]"
+ "carKeyDowngradeVersionSetting:brand:uuid:reply:"
+ "Failed to get Endpoint Manager"
- "/System/Library/CoreServices/SystemVersion.plist"
- "CFStringGetTypeID"
- "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
- "iOS (18.1) - SecureElementService-51.5.1"
- "CFDictionaryGetValue"
- "unlockFromOtherSource"
- "CFStringCreateWithCStringNoCopy"
- "kCFAllocatorNull"
- "rangingExceptionTriggered"
- "CFPropertyListCreateWithData"
- "r"
- "_Concurrency/TaskGroup.swift"
- "CFStringGetCString"
- "CFGetTypeID"
- "CFRelease"
- "CFPropertyListCreateFromXMLData"
- "ProductVersion"
- "CFDataCreateWithBytesNoCopy"
- "\r\x13"

```

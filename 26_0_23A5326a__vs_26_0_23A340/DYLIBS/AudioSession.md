## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

 398.110.32.0.0
-  __TEXT.__text: 0x49c34
+  __TEXT.__text: 0x49ff8
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x21c8
-  __TEXT.__gcc_except_tab: 0x88c0
-  __TEXT.__cstring: 0x285c
+  __TEXT.__objc_methlist: 0x21e0
+  __TEXT.__gcc_except_tab: 0x893c
+  __TEXT.__cstring: 0x2879
   __TEXT.__const: 0x21f
   __TEXT.__oslogstring: 0x35ea
   __TEXT.__unwind_info: 0x2b80
   __TEXT.__objc_classname: 0x51b
-  __TEXT.__objc_methname: 0x4f67
+  __TEXT.__objc_methname: 0x4fbd
   __TEXT.__objc_methtype: 0x1ec2
-  __TEXT.__objc_stubs: 0x2c20
-  __DATA_CONST.__got: 0xae8
+  __TEXT.__objc_stubs: 0x2c40
+  __DATA_CONST.__got: 0xb00
   __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1588
+  __DATA_CONST.__objc_selrefs: 0x1598
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x1698
   __AUTH_CONST.__cfstring: 0x20a0
-  __AUTH_CONST.__objc_const: 0x2778
+  __AUTH_CONST.__objc_const: 0x27a8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x538
   __DATA.__common: 0x1
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x2d0
+  __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CBEB0FA-C427-3D79-B4E1-D7976BCFA52A
-  Functions: 1581
-  Symbols:   5598
-  CStrings:  1894
+  UUID: 00E4E088-BA90-3E16-82E6-45A5D2907E52
+  Functions: 1583
+  Symbols:   5611
+  CStrings:  1899
 
Symbols:
+ -[AVAudioSessionPortExtensionBluetoothMicrophone farFieldCapture]
+ -[AVAudioSessionPortExtensionBluetoothMicrophone setFarFieldCapture:]
+ _OBJC_IVAR_$_AVAudioSessionPortExtensionBluetoothMicrophone.farFieldCapture
+ __ZGVZN4avasL20FarFieldInputEnabledEvE20farFieldInputEnabled
+ __ZZN4avasL20FarFieldInputEnabledEvE20farFieldInputEnabled
+ _kMXSessionProperty_PrefersBluetoothFarFieldCapture
+ _kMXSession_RouteDetailedDescriptionKey_IsFarFieldCaptureEnabled
+ _kMXSession_RouteDetailedDescriptionKey_SupportsFarFieldCapture
+ _objc_msgSend$setFarFieldCapture:
Functions:
~ __ZN4avas6client11SessionCore30addCategoryOptionsToDictionaryEP19NSMutableDictionaryP8NSStringm : 1860 -> 2212
+ -[AVAudioSessionPortExtensionBluetoothMicrophone farFieldCapture]
+ -[AVAudioSessionPortExtensionBluetoothMicrophone .cxx_destruct]
~ -[AVAudioSessionPortDescription initWithRawPortDescriptionXPC:owningSession:] : 2872 -> 3264
~ __ZNK4avas6client11SessionCore15categoryOptionsEv : 704 -> 848
CStrings:
+ "T@\"AVAudioSessionCapability\",&,N,VfarFieldCapture"
+ "Translate"
+ "farFieldCapture"
+ "personalTranslator"
+ "setFarFieldCapture:"

```

## AHTUserEventAgent

> `/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent`

```diff

 8150.1.0.0.0
-  __TEXT.__text: 0x47fc
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__text: 0x61c0
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0xa80
   __TEXT.__objc_methlist: 0x52c
-  __TEXT.__cstring: 0x990
+  __TEXT.__cstring: 0xb78
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x368
-  __TEXT.__objc_methname: 0xca2
-  __TEXT.__const: 0x40
+  __TEXT.__objc_methname: 0xcf6
+  __TEXT.__const: 0x240
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__oslogstring: 0x42c
-  __TEXT.__unwind_info: 0x170
-  __DATA.__auth_got: 0x2a0
-  __DATA.__got: 0x90
-  __DATA.__const: 0x118
-  __DATA.__cfstring: 0xa00
+  __TEXT.__oslogstring: 0x602
+  __TEXT.__unwind_info: 0x1b0
+  __DATA.__auth_got: 0x2f8
+  __DATA.__got: 0xa0
+  __DATA.__const: 0x1e0
+  __DATA.__cfstring: 0xb80
   __DATA.__objc_classlist: 0x28
   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x10
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xc10
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_selrefs: 0x3e0
   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x190
   __DATA.__objc_intobj: 0x4e0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x3e0
   __DATA.__objc_arraydata: 0x10
   __DATA.__objc_arrayobj: 0x18
   __DATA.__bss: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 113
-  Symbols:   120
-  CStrings:  368
+  Functions: 137
+  Symbols:   152
+  CStrings:  427
 
Symbols:
+ _CFStringHasPrefix
+ _CRWasComponentRepaired
+ _DERDecodeItem
+ _DERDecodeItemPartialBuffer
+ _DERDecodeItemPartialBufferGetLength
+ _DERDecodeSeqContentInit
+ _DERDecodeSeqInit
+ _DERDecodeSeqNext
+ _DERDecodeSequenceContentWithBlock
+ _DERDecodeSequenceWithBlock
+ _DERParseBitString
+ _DERParseBoolean
+ _DERParseBooleanWithDefault
+ _DERParseInteger
+ _DERParseInteger64
+ _DERParseSequence
+ _DERParseSequenceContent
+ _DERParseSequenceContentToObject
+ _DERParseSequenceToObject
+ _IORegistryEntryFromPath
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_NSData
+ _bzero
+ _isDataInRCHL
+ _kIOMainPortDefault
+ _memcmp
+ _objc_release_x28
+ _objc_retain_x27
+ _objc_retain_x28
+ _printf
+ _strncmp
+ _strnlen
CStrings:
+ "%.*s\n"
+ "%s Fail to convert dictionary for repair history node dictionary"
+ "%s Fail to find bootloader"
+ "%s Fail to find bootloader registry properties"
+ "%s Fail to find device"
+ "%s Fail to find propertySource"
+ "%s Fail to find repair history node"
+ "%s Fail to get property list for repair history node"
+ "%s MtDO Invalidation Stat Collection Done"
+ "%s collectRepairHistoryInvalidationStat"
+ "%s isCoverGlassRepaired = %x"
+ "%s isDisplayRepaired = %x"
+ "%s isMtDOCalPresent = %x"
+ "%s isMtDOInvalidated = %x"
+ "-[AHTDeviceStats collectRepairHistoryInvalidationStat]"
+ "AlsC"
+ "BackGlass"
+ "Battery"
+ "Camera"
+ "Checking for %s\n"
+ "CmCl"
+ "CoverGlass"
+ "CoverGlassRepaired"
+ "Default"
+ "Display"
+ "DisplayRepaired"
+ "FSCl"
+ "FaceID"
+ "HWModelStr"
+ "Invalid parameters: %p, %p, %lu\n"
+ "Invalidated"
+ "IsMtDOCalPresent"
+ "J481"
+ "J482"
+ "LCfg"
+ "MTUB"
+ "McTUB"
+ "Property Sources"
+ "SrvP"
+ "TouchID"
+ "Unknown component: %s\n"
+ "VolumeButton"
+ "bCfg"
+ "bcrt"
+ "bytes"
+ "com.apple.multitouch.calInvalidation.MtDO"
+ "dCfg"
+ "dataWithBytes:length:"
+ "found data %s\n"
+ "getRegistryProperties"
+ "isEqualToString:"
+ "length"
+ "multitouch-to-display-offset"
+ "prpc"
+ "psd2"
+ "repair-history"
+ "tcrt"
+ "vcrt"
+ "withName:"

```

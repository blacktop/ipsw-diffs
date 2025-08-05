## CoreMIDI

> `/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI`

```diff

-322.0.0.0.0
-  __TEXT.__text: 0xa4eec
+324.0.0.0.0
+  __TEXT.__text: 0xa5c38
   __TEXT.__auth_stubs: 0x1d50
   __TEXT.__objc_methlist: 0x15a0
   __TEXT.__const: 0x9b4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0xdd50
-  __TEXT.__cstring: 0x44e7
-  __TEXT.__oslogstring: 0x2b44
+  __TEXT.__gcc_except_tab: 0xde20
+  __TEXT.__cstring: 0x44f5
+  __TEXT.__oslogstring: 0x2b71
   __TEXT.__unwind_info: 0x3eb0
   __TEXT.__objc_classname: 0x1f4
   __TEXT.__objc_methname: 0x2dd9

   __AUTH_CONST.__cfstring: 0x1a60
   __AUTH_CONST.__objc_const: 0x2660
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x13e8
   __DATA.__common: 0x188
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0F7AEA0-90EF-3DBC-8D91-720626292054
+  UUID: 545B5325-C766-3293-90BD-8929080AC56E
   Functions: 2631
   Symbols:   7866
-  CStrings:  1899
+  CStrings:  1901
 
Symbols:
+ ___block_descriptor_tmp.3876
- ___block_descriptor_tmp.3874
Functions:
~ __ZN9XPCClient32UMPCIServerSideMIDICITransactionEPK14__CFDictionaryPS2_ : 1044 -> 1056
~ __ZN9XPCClient25UMPCIObjectSetDescriptionEjPK14__CFDictionary : 736 -> 752
~ __ZN9XPCClient17UMPCIObjectCreateE15UMPCIObjectTypePK14__CFDictionaryPj : 784 -> 796
~ __ZN9XPCClient24MIDIObjectRemovePropertyEjPK10__CFString : 548 -> 916
~ __ZN9XPCClient31MIDIObjectSetDictionaryPropertyEjPK10__CFStringPK14__CFDictionary : 980 -> 1408
~ __ZN9XPCClient31MIDIObjectGetDictionaryPropertyEjPK10__CFStringPPK14__CFDictionary : 884 -> 1244
~ __ZN9XPCClient25MIDIObjectSetDataPropertyEjPK10__CFStringPK8__CFData : 648 -> 1012
~ __ZN9XPCClient25MIDIObjectGetDataPropertyEjPK10__CFStringPPK8__CFData : 840 -> 1192
~ __ZN9XPCClient27MIDIObjectSetStringPropertyEjPK10__CFStringS2_ : 808 -> 1208
~ __ZN9XPCClient27MIDIObjectGetStringPropertyEjPK10__CFStringPS2_ : 992 -> 1380
~ __ZN9XPCClient28MIDIObjectSetIntegerPropertyEjPK10__CFStringi : 580 -> 928
~ __ZN9XPCClient28MIDIObjectGetIntegerPropertyEjPK10__CFStringPi : 596 -> 952
CStrings:
+ "%25s:%-5d std::runtime_error in API call: %s"
+ "XPCClient.hpp"

```

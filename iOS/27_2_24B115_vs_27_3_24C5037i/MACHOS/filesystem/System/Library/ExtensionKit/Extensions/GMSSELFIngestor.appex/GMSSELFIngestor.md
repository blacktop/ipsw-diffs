## GMSSELFIngestor

> `/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/GMSSELFIngestor`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-3605.4.1.0.0
-  __TEXT.__text: 0x16d5c
-  __TEXT.__auth_stubs: 0xd20
+3610.4.1.0.0
+  __TEXT.__text: 0x16f34
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x780
   __TEXT.__const: 0x3b8
   __TEXT.__swift5_typeref: 0x2b5

   __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x158
   __DATA.__objc_const: 0x4d0
   __DATA.__objc_selrefs: 0x1e0
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x578
+  __DATA.__data: 0x580
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
+  - /System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 133
-  Symbols:   136
+  Symbols:   137
   CStrings:  180
 
Symbols:
+ _swift_retain_x25
Functions:
~ sub_100013660 -> sub_1000136e0 : 11344 -> 11816
```

## SatelliteSMS

> `/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS`

```diff

-1402.200.8.0.0
-  __TEXT.__text: 0xbee8
-  __TEXT.__auth_stubs: 0xac0
+1402.200.35.0.0
+  __TEXT.__text: 0xc38c
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x38a
   __TEXT.__objc_methname: 0xfbc
-  __TEXT.__oslogstring: 0x7fc
-  __TEXT.__cstring: 0x681
+  __TEXT.__oslogstring: 0x86c
+  __TEXT.__cstring: 0x6a1
   __TEXT.__swift5_typeref: 0x17e
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_capture: 0x1c

   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_reflstr: 0x43
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x288
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x558
   __DATA_CONST.__cfstring: 0xa0

   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 188
-  Symbols:   193
-  CStrings:  297
+  Functions: 189
+  Symbols:   198
+  CStrings:  301
 
Symbols:
+ _CMFItemCreateWithPhoneNumber
+ _IMSetDomainBoolForKey
+ _IMPhoneNumberRefCopyForPhoneNumber
+ _kSMSSatelliteNeedsRelay
+ _CMFBlockListIsItemBlocked
CStrings:
+ "Couldn't create phone item."
+ "Couldn't create phone number."
+ "Message is blocked for sender handle: %!s(MISSING)"
+ "com.apple.madrid"

```

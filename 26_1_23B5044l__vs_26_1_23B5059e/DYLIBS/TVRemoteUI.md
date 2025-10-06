## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-548.10.16.0.0
-  __TEXT.__text: 0xcd520
+548.10.21.0.0
+  __TEXT.__text: 0xcd4b8
   __TEXT.__auth_stubs: 0x1b30
   __TEXT.__objc_methlist: 0xb3e0
   __TEXT.__const: 0x24a4
   __TEXT.__gcc_except_tab: 0x1ec4
-  __TEXT.__cstring: 0x745a
+  __TEXT.__cstring: 0x740a
   __TEXT.__oslogstring: 0x59c2
   __TEXT.__ustring: 0x4a
   __TEXT.__dlopen_cstrs: 0x4e

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2ac8
+  __TEXT.__unwind_info: 0x2ac0
   __TEXT.__eh_frame: 0x878
   __TEXT.__objc_classname: 0x144f
-  __TEXT.__objc_methname: 0x1b1ed
+  __TEXT.__objc_methname: 0x1b1d9
   __TEXT.__objc_methtype: 0x44c7
-  __TEXT.__objc_stubs: 0x12fe0
+  __TEXT.__objc_stubs: 0x13000
   __DATA_CONST.__got: 0xd38
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x5a0

   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0xda8
   __AUTH_CONST.__const: 0x2eb8
-  __AUTH_CONST.__cfstring: 0x3a20
-  __AUTH_CONST.__objc_const: 0x14a08
+  __AUTH_CONST.__cfstring: 0x3a00
+  __AUTH_CONST.__objc_const: 0x14a20
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8

   __AUTH.__data: 0x588
   __DATA.__objc_ivar: 0xb44
   __DATA.__data: 0x2538
-  __DATA.__bss: 0x2658
+  __DATA.__bss: 0x2668
   __DATA.__common: 0x4c8
   __DATA_DIRTY.__objc_data: 0x7d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F9DE9F88-3FD9-3A45-BE2D-4B846222C04F
-  Functions: 4702
-  Symbols:   17462
-  CStrings:  7205
+  UUID: 7F579B95-9C14-3293-91F6-585E393EEF17
+  Functions: 4701
+  Symbols:   17463
+  CStrings:  7204
 
Symbols:
+ +[TVRUIFeatures _prefForKey:]
+ +[TVRUIFeatures defaults]
+ __OBJC_$_CLASS_PROP_LIST_TVRUIFeatures
+ __defaults
+ _objc_msgSend$_prefForKey:
+ _objc_msgSend$defaults
+ _objc_msgSend$initWithSuiteName:
- +[TVRUIFeatures _globalPrefForKey:]
- +[TVRUIFeatures isWakeToRemoteOnLockScreenDisabled]
- ___51+[TVRUIFeatures isWakeToRemoteOnLockScreenDisabled]_block_invoke
- _objc_msgSend$_globalPrefForKey:
- _objc_msgSend$dictionaryWithContentsOfFile:
CStrings:
+ "T@\"NSUserDefaults\",R,N"
+ "_prefForKey:"
+ "com.apple.TVRemoteCore"
+ "defaults"
+ "initWithSuiteName:"
- "/var/mobile/Library/Preferences/.GlobalPreferences.plist"
- "TVRemoteWakeToRemoteOnLockScreenDisabled"
- "_globalPrefForKey:"
- "dictionaryWithContentsOfFile:"
- "isWakeToRemoteOnLockScreenDisabled"

```

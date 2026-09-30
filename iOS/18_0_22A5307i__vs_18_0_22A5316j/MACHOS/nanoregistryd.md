## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-978.0.0.0.0
-  __TEXT.__text: 0xf54b0
+980.0.0.0.0
+  __TEXT.__text: 0xf59b0
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x106a0
-  __TEXT.__objc_methlist: 0xbc78
+  __TEXT.__objc_stubs: 0x106e0
+  __TEXT.__objc_methlist: 0xbc98
   __TEXT.__const: 0x678
-  __TEXT.__gcc_except_tab: 0x2418
-  __TEXT.__objc_methname: 0x1b377
-  __TEXT.__cstring: 0xcf95
-  __TEXT.__oslogstring: 0x130bb
-  __TEXT.__objc_classname: 0x2176
+  __TEXT.__gcc_except_tab: 0x248c
+  __TEXT.__objc_methname: 0x1b3d0
+  __TEXT.__cstring: 0xcfc6
+  __TEXT.__oslogstring: 0x13160
+  __TEXT.__objc_classname: 0x2177
   __TEXT.__objc_methtype: 0x493f
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
   __TEXT.__info_plist: 0x401
-  __TEXT.__unwind_info: 0x3850
+  __TEXT.__unwind_info: 0x3870
   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xc18
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x4928
-  __DATA_CONST.__cfstring: 0xb900
+  __DATA_CONST.__cfstring: 0xb920
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1beb8
-  __DATA.__objc_selrefs: 0x5890
-  __DATA.__objc_ivar: 0x1130
+  __DATA.__objc_const: 0x1bf38
+  __DATA.__objc_selrefs: 0x58a0
+  __DATA.__objc_ivar: 0x1140
   __DATA.__objc_data: 0x4c40
   __DATA.__data: 0x19d8
   __DATA.__bss: 0x498

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5561
+  Functions: 5564
   Symbols:   677
-  CStrings:  8399
+  CStrings:  8408
 
CStrings:
+ "\x02\x11\x13"
+ "280"
+ "Found stashed peer, retrying"
+ "Missed BT timer fired, resetting stashed variables"
+ "NanoRegistry-980"
+ "Reuse existing NRDevicePairingManager to scan for candiates"
+ "Unable to handle pairing request.  Stashing to try again later"
+ "_startScanningForCandidates"
+ "_stashedPassKey"
+ "_stashedPeer"
+ "_stashedType"
+ "com.apple.nanoregistry.migration.missedbtrequest"
+ "resetStashVaribles"
- "\x02\x11"
- "244"
- "NanoRegistry-978"
- "Reuse existing NRDevicePairingManager"

```

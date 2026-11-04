## AppleIDSetupDaemon

> `/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon`

```diff

-129.125.7.1.0
-  __TEXT.__text: 0x19eac4
+129.250.2.0.0
+  __TEXT.__text: 0x1a11fc
   __TEXT.__objc_methlist: 0x8ac
-  __TEXT.__const: 0x4a64
+  __TEXT.__const: 0x4a84
   __TEXT.__cstring: 0xb22
-  __TEXT.__oslogstring: 0x9b0f
-  __TEXT.__constg_swiftt: 0x1e90
-  __TEXT.__swift5_typeref: 0x1ebe
+  __TEXT.__oslogstring: 0x9e0f
+  __TEXT.__constg_swiftt: 0x1eb8
+  __TEXT.__swift5_typeref: 0x1ed0
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x11ee
-  __TEXT.__swift5_fieldmd: 0x1030
+  __TEXT.__swift5_reflstr: 0x1222
+  __TEXT.__swift5_fieldmd: 0x1048
   __TEXT.__swift5_assocty: 0x300
-  __TEXT.__swift5_capture: 0xf78
+  __TEXT.__swift5_capture: 0xf9c
   __TEXT.__swift5_proto: 0x1c8
   __TEXT.__swift5_types: 0x114
-  __TEXT.__swift_as_entry: 0x570
-  __TEXT.__swift_as_ret: 0xaa8
-  __TEXT.__swift_as_cont: 0x1520
+  __TEXT.__swift_as_entry: 0x574
+  __TEXT.__swift_as_ret: 0xab4
+  __TEXT.__swift_as_cont: 0x1530
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x61d0
-  __TEXT.__eh_frame: 0x16e40
+  __TEXT.__unwind_info: 0x6230
+  __TEXT.__eh_frame: 0x16ff0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_selrefs: 0x768
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0xd98
-  __AUTH_CONST.__const: 0x33f8
+  __DATA_CONST.__got: 0xde0
+  __AUTH_CONST.__const: 0x3448
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x3e20
-  __AUTH_CONST.__auth_got: 0x1748
+  __AUTH_CONST.__objc_const: 0x3e60
+  __AUTH_CONST.__auth_got: 0x1798
   __AUTH.__objc_data: 0x558
-  __AUTH.__data: 0xee0
+  __AUTH.__data: 0xef0
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1b30
+  __DATA.__data: 0x1b18
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x290
+  __DATA_DIRTY.__objc_data: 0x2b8
   __DATA_DIRTY.__data: 0x8c8
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4024
-  Symbols:   1092
-  CStrings:  754
+  Functions: 4039
+  Symbols:   1097
+  CStrings:  764
 
Symbols:
+ _ACAccountTypeIdentifierIdentityServices
+ _AIDAServiceTypeFaceTime
+ _AIDAServiceTypeMessages
+ _symbolic SSSgz_Xx
+ _symbolic ______p 12AppleIDSetup28AnalyticsReporterRTCProtocolP
CStrings:
+ "Checking for IdentityServices account"
+ "Did not find an IdentityServices account matching the primary Apple Account"
+ "Discovered eligible IdentityServices account for the primary Apple Account"
+ "Explicitly adding Messages and FaceTime to services for IdMS account, only as a temporary workaround"
+ "Failed to fetch IdentityServices accounts: %@"
+ "Failed to start proximity connector: %@"
+ "No primary AuthKit account found on device. Cannot search for IdentityServices account."
+ "Primary AuthKit account has no DSID. Cannot search for IdentityServices account."
+ "Primary AuthKit account has no altDSID. Cannot search for IdentityServices account."
+ "Proximity connector started and listening for IDS messages"
```

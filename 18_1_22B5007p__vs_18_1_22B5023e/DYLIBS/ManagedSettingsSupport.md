## ManagedSettingsSupport

> `/System/Library/PrivateFrameworks/ManagedSettingsSupport.framework/ManagedSettingsSupport`

```diff

-214.0.0.0.0
+215.0.0.0.0
   __TEXT.__text: 0x8088
   __TEXT.__auth_stubs: 0x700
   __TEXT.__const: 0xafa

   __TEXT.__eh_frame: 0x608
   __TEXT.__objc_methname: 0x6d
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 287
-  Symbols:   72
-  CStrings:  0
+  Symbols:   80
+  CStrings:  13
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "S_$_NEInternetNexus"
+ "_OBJC_CLASS_$_NEKeychainItem"
+ "_OBJC_CLASS_$_NELoopbackConnection"
+ "_OBJC_CLASS_$_NENexus"
+ "_OBJC_CLASS_$_NENexusAgent"
+ "_OBJC_CLASS_$_NENexusBrowse"
+ "_OBJC_CLASS_$_NENexusFlow"
+ "_OBJC_CLASS_$_NENexusFlowAssignedProperties"
+ "_OBJC_CLASS_$_NENexusFlowDivertFlow"
+ "_OBJC_CLASS_$_NENexusFlowManager"
+ "_OBJC_METACLASS_$_NEIKEv2InitiatorTransportIPv6Address"
+ "_OBJC_METACLASS_$_NEIKEv2Listener"
+ "alContext"

```
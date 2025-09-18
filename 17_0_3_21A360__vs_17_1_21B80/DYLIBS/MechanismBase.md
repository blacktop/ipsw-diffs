## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-1391.2.1.0.0
-  __TEXT.__text: 0x9e8c
+1394.40.33.0.0
+  __TEXT.__text: 0xa6d4
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0xb18
-  __TEXT.__const: 0x98
+  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0x70c
-  __TEXT.__oslogstring: 0x913
-  __TEXT.__unwind_info: 0x360
-  __TEXT.__objc_classname: 0x15e
-  __TEXT.__objc_methname: 0x2593
-  __TEXT.__objc_methtype: 0x83b
-  __TEXT.__objc_stubs: 0x17a0
+  __TEXT.__cstring: 0x769
+  __TEXT.__oslogstring: 0x974
+  __TEXT.__unwind_info: 0x38c
+  __TEXT.__objc_classname: 0x171
+  __TEXT.__objc_methname: 0x2749
+  __TEXT.__objc_methtype: 0x86d
+  __TEXT.__objc_stubs: 0x1900
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3a8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a60
-  __DATA_CONST.__objc_selrefs: 0x878
+  __DATA_CONST.__objc_const: 0x1b98
+  __DATA_CONST.__objc_selrefs: 0x8e0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_const: 0x480
-  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__objc_const: 0x4c8
+  __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__auth_got: 0x288
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_superrefs: 0x50
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D2B14B9-23C6-3107-9B5F-4E2A850C7BE7
-  Functions: 283
-  Symbols:   1132
-  CStrings:  750
+  UUID: 50A48D07-DE2E-3D57-ADE9-5656BF7E7ADA
+  Functions: 301
+  Symbols:   1192
+  CStrings:  788
 
Symbols:
+ -[MechanismAssertion .cxx_destruct]
+ -[MechanismAssertion _assertInStateAndStartMonitoring]
+ -[MechanismAssertion _startMonitoringIfNeeded]
+ -[MechanismAssertion _stopMonitoringIfNeeded]
+ -[MechanismAssertion acquireWithReason:error:]
+ -[MechanismAssertion assertInState]
+ -[MechanismAssertion dealloc]
+ -[MechanismAssertion description]
+ -[MechanismAssertion dropWithReason:]
+ -[MechanismAssertion handleAssertionFailureWithReason:error:]
+ -[MechanismAssertion handleAssertionFailureWithReason:error:].cold.1
+ -[MechanismAssertion handleAssertionSuccessWithReason:]
+ -[MechanismAssertion initWithMechanism:]
+ -[MechanismAssertion log]
+ -[MechanismAssertion mechanism]
+ -[MechanismAssertion startMonitoring]
+ -[MechanismAssertion stopMonitoring]
+ -[MechanismKofN setParent:]
+ _OBJC_CLASS_$_MechanismAssertion
+ _OBJC_IVAR_$_MechanismAssertion._acquired
+ _OBJC_IVAR_$_MechanismAssertion._log
+ _OBJC_IVAR_$_MechanismAssertion._mechanism
+ _OBJC_IVAR_$_MechanismAssertion._mechanismInitialDescription
+ _OBJC_IVAR_$_MechanismAssertion._monitoring
+ _OBJC_IVAR_$_MechanismBase._mechanismAssertions
+ _OBJC_METACLASS_$_MechanismAssertion
+ __OBJC_$_INSTANCE_METHODS_MechanismAssertion
+ __OBJC_$_INSTANCE_VARIABLES_MechanismAssertion
+ __OBJC_$_PROP_LIST_MechanismAssertion
+ __OBJC_CLASS_RO_$_MechanismAssertion
+ __OBJC_METACLASS_RO_$_MechanismAssertion
+ _objc_msgSend$_assertInStateAndStartMonitoring
+ _objc_msgSend$_startMonitoringIfNeeded
+ _objc_msgSend$_stopMonitoringIfNeeded
+ _objc_msgSend$assertInState
+ _objc_msgSend$description
+ _objc_msgSend$dropWithReason:
+ _objc_msgSend$handleAssertionFailureWithReason:error:
+ _objc_msgSend$handleAssertionSuccessWithReason:
+ _objc_msgSend$mechanism
+ _objc_msgSend$startMonitoring
+ _objc_msgSend$stopMonitoring
CStrings:
+ "\x05!1\x11\x126"
+ "%@ (post dealloc)"
+ "%{public}@ confirmed (%{public}@)"
+ "%{public}@ dropped (%{public}@)"
+ "%{public}@ failed (%{public}@)"
+ "<%@ on %@>"
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSString\""
+ "B32@0:8@16^@24"
+ "MechanismAssertion"
+ "T@\"MechanismBase\",R,W,N,V_mechanism"
+ "T@\"NSObject<OS_os_log>\",R,N,V_log"
+ "_acquired"
+ "_assertInStateAndStartMonitoring"
+ "_log"
+ "_mechanism"
+ "_mechanismAssertions"
+ "_mechanismInitialDescription"
+ "_monitoring"
+ "_startMonitoringIfNeeded"
+ "_stopMonitoringIfNeeded"
+ "aQC"
+ "acquireWithReason:error:"
+ "assertInState"
+ "dealloc"
+ "dropWithReason:"
+ "failed acquisition for %@"
+ "handleAssertionFailureWithReason:error:"
+ "handleAssertionSuccessWithReason:"
+ "initWithMechanism:"
+ "mechanism"
+ "startMonitoring"
+ "stopMonitoring"
+ "successful acquisition for %@"
- "\x04!1\x11\x126"
- "QQC"

```

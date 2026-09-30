## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-781.0.0.0.1
-  __TEXT.__text: 0x6b988
+784.40.1.0.0
+  __TEXT.__text: 0x6c730
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x4238
+  __TEXT.__objc_methlist: 0x4308
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xed03
-  __TEXT.__oslogstring: 0x7c82
-  __TEXT.__gcc_except_tab: 0x1e40
+  __TEXT.__cstring: 0xef66
+  __TEXT.__oslogstring: 0x7e1c
+  __TEXT.__gcc_except_tab: 0x1e58
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1850
-  __TEXT.__objc_classname: 0x8df
-  __TEXT.__objc_methname: 0xafca
-  __TEXT.__objc_methtype: 0x2416
-  __TEXT.__objc_stubs: 0x6180
-  __DATA_CONST.__got: 0x3f8
+  __TEXT.__unwind_info: 0x1880
+  __TEXT.__objc_classname: 0x92d
+  __TEXT.__objc_methname: 0xb2c3
+  __TEXT.__objc_methtype: 0x24e5
+  __TEXT.__objc_stubs: 0x6340
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0x1be8
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2118
+  __DATA_CONST.__objc_selrefs: 0x2198
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5ae0
-  __AUTH_CONST.__objc_const: 0xaf50
+  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__objc_const: 0xb3d8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x224
-  __DATA.__data: 0x908
-  __DATA.__bss: 0x68
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x22c
+  __DATA.__data: 0x9c8
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10654977-D251-353D-978B-666E3EBFE737
-  Functions: 1998
-  Symbols:   6601
-  CStrings:  4225
+  UUID: FDC247F3-FD3C-3355-9DA2-55457C6EA5D1
+  Functions: 2016
+  Symbols:   6676
+  CStrings:  4278
 
Symbols:
+ -[IXTerminationAssertion .cxx_destruct]
+ -[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:]
+ -[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:].cold.1
+ -[IXTerminationAssertion acquireAssertion:]
+ -[IXTerminationAssertion acquireAssertion:].cold.1
+ -[IXTerminationAssertion assertionTargetProcessDidExit:]
+ -[IXTerminationAssertion assertionTargetProcessDidExit:].cold.1
+ -[IXTerminationAssertion dealloc]
+ -[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:]
+ -[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:].cold.1
+ -[IXTerminationAssertion invalidate]
+ -[IXTerminationAssertion setTermAssertion:]
+ -[IXTerminationAssertion setTermAssertion:].cold.1
+ -[IXTerminationAssertion termAssertion]
+ -[IXTerminationAssertion waitForAssertionSemaphore]
+ -[IXUnregisterOSModuleToken acquireTerminationAssertionsWithError:]
+ -[IXUnregisterOSModuleToken acquireTerminationAssertionsWithError:].cold.1
+ -[IXUnregisterOSModuleToken setTerminationAssertion:]
+ -[IXUnregisterOSModuleToken terminationAssertion]
+ _OBJC_CLASS_$_IXTerminationAssertion
+ _OBJC_CLASS_$_RBSTerminationAssertion
+ _OBJC_IVAR_$_IXTerminationAssertion._termAssertion
+ _OBJC_IVAR_$_IXTerminationAssertion._waitForAssertionSemaphore
+ _OBJC_IVAR_$_IXUnregisterOSModuleToken._terminationAssertion
+ _OBJC_METACLASS_$_IXTerminationAssertion
+ __OBJC_$_INSTANCE_METHODS_IXTerminationAssertion
+ __OBJC_$_INSTANCE_VARIABLES_IXTerminationAssertion
+ __OBJC_$_PROP_LIST_IXTerminationAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RBSAssertionObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RBSTerminationAssertionObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RBSAssertionObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RBSTerminationAssertionObserving
+ __OBJC_$_PROTOCOL_REFS_RBSAssertionObserving
+ __OBJC_$_PROTOCOL_REFS_RBSTerminationAssertionObserving
+ __OBJC_CLASS_PROTOCOLS_$_IXTerminationAssertion
+ __OBJC_CLASS_RO_$_IXTerminationAssertion
+ __OBJC_LABEL_PROTOCOL_$_RBSAssertionObserving
+ __OBJC_LABEL_PROTOCOL_$_RBSTerminationAssertionObserving
+ __OBJC_METACLASS_RO_$_IXTerminationAssertion
+ __OBJC_PROTOCOL_$_RBSAssertionObserving
+ __OBJC_PROTOCOL_$_RBSTerminationAssertionObserving
+ ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.5
+ ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.5.cold.1
+ _objc_msgSend$_terminationAssertionForBundleIDs:description:terminationResistance:error:
+ _objc_msgSend$acquireAssertion:
+ _objc_msgSend$acquireTerminationAssertionsWithError:
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$enumeratorForApplicationsOnSameVolumeWithinDirectoryAtURL:enumerationOptions:filteringOptions:
+ _objc_msgSend$initForBundleIDs:description:terminationResistance:error:
+ _objc_msgSend$predicateMatchingBundleIdentifiers:
+ _objc_msgSend$setTermAssertion:
+ _objc_msgSend$setTerminationAssertion:
+ _objc_msgSend$termAssertion
+ _objc_msgSend$terminationAssertion
+ _objc_msgSend$waitForAssertionSemaphore
- -[IXUnregisterOSModuleToken setIsValid:]
- _OBJC_IVAR_$_IXUnregisterOSModuleToken._isValid
- ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.4
- ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.4.cold.1
CStrings:
+ "%s failed in init"
+ "%s: %s failed in init : %@"
+ "%s: Attempting to set the same termination assertion for %@"
+ "%s: Failed to acquire termination assertion %@ : %@"
+ "%s: Failed to create termination assertion for predicate %@ : %@"
+ "%s: Failed to enumerate apps on module at %@ : %@"
+ "%s: RBS termination assertion observer called for %@"
+ "%s: We didn't have a termination assertion that we're tracking, so not acting on the callback from RBS"
+ "-[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:]"
+ "-[IXTerminationAssertion acquireAssertion:]"
+ "-[IXTerminationAssertion assertionTargetProcessDidExit:]"
+ "-[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:]"
+ "-[IXTerminationAssertion setTermAssertion:]"
+ "-[IXUnregisterOSModuleToken acquireTerminationAssertionsWithError:]"
+ "@\"IXTerminationAssertion\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"RBSTerminationAssertion\""
+ "@44@0:8@16@24C32^@36"
+ "Failed to acquire termination assertion %@"
+ "Failed to create termination assertion for predicate %@"
+ "Failed to enumerate apps on module at %@"
+ "IXTerminationAssertion"
+ "RBSAssertionObserving"
+ "RBSTerminationAssertionObserving"
+ "T@\"IXTerminationAssertion\",&,N,V_terminationAssertion"
+ "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_waitForAssertionSemaphore"
+ "T@\"RBSTerminationAssertion\",&,N,V_termAssertion"
+ "_termAssertion"
+ "_terminationAssertion"
+ "_terminationAssertionForBundleIDs:description:terminationResistance:error:"
+ "_waitForAssertionSemaphore"
+ "acquireAssertion:"
+ "acquireTerminationAssertionsWithError:"
+ "acquireWithError:"
+ "addObserver:"
+ "assertion:didInvalidateWithError:"
+ "assertionTargetProcessDidExit:"
+ "assertionWillInvalidate:"
+ "bundleIdentifier"
+ "enumeratorForApplicationsOnSameVolumeWithinDirectoryAtURL:enumerationOptions:filteringOptions:"
+ "initForBundleIDs:description:terminationResistance:error:"
+ "installcoordinationd os-module-unregister moduleURL:%@"
+ "predicateMatchingBundleIdentifiers:"
+ "setTermAssertion:"
+ "setTerminationAssertion:"
+ "termAssertion"
+ "terminationAssertion"
+ "v24@0:8@\"RBSAssertion\"16"
+ "v24@0:8@\"RBSTerminationAssertion\"16"
+ "v32@0:8@\"RBSAssertion\"16@\"NSError\"24"
+ "waitForAssertionSemaphore"
- "TB,N,V_isValid"
- "_isValid"
- "setIsValid:"

```

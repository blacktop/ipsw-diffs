## CommCenterRootHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper`

```diff

-12410.0.0.0.0
-  __TEXT.__text: 0x1a38
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__const: 0x53
-  __TEXT.__cstring: 0xd9
-  __TEXT.__oslogstring: 0xd4
+13071.5.0.0.0
+  __TEXT.__text: 0x4284
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__gcc_except_tab: 0x58c
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x530
+  __TEXT.__oslogstring: 0x258
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x350
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0x310
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 810CD0C1-7243-3A1F-8DC3-C3580935EDF1
-  Functions: 44
-  Symbols:   82
-  CStrings:  15
+  UUID: 96E55577-2156-39FF-9666-5BE1098527EC
+  Functions: 84
+  Symbols:   132
+  CStrings:  102
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFArrayCreate
+ _CFBooleanGetTypeID
+ _CFDictionaryGetValue
+ _CFGetTypeID
+ _CFRelease
+ _CFStringCompare
+ _CFStringGetTypeID
+ _MGCopyMultipleAnswers
+ _TelephonyUtilIsOversteerEnabled
+ __ZN12TelephonyXPC6Server17setCommandHandlerENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvNS_17ServerClientStateEN3xpc4dictENS9_IU13block_pointerFviSC_EEEEEE
+ __ZN3abm12HelperServer6createEv
+ __ZN3ctu2cf6assignERbPK11__CFBoolean
+ __ZN3xpc19dyn_cast_or_defaultERKNS_6objectEPKc
+ __ZN3xpc19dyn_cast_or_defaultERKNS_6objectEb
+ __ZN3xpc19dyn_cast_or_defaultERKNS_6objectEi
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZNSt3__19to_stringEi
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZTISt12length_error
+ __ZTVSt12length_error
+ __ZnwmSt19__type_descriptor_t
+ ___CFConstantStringClassReference
+ ___assert_rtn
+ ___error
+ _bzero
+ _dispatch_async
+ _ether_ntoa
+ _execv
+ _exit
+ _fork
+ _free
+ _freeifaddrs
+ _getifaddrs
+ _getpid
+ _kCFTypeArrayCallBacks
+ _malloc_type_malloc
+ _memchr
+ _memmove
+ _pthread_once
+ _setsid
+ _snprintf
+ _strcmp
+ _strerror
+ _strlen
+ _sysctlbyname
+ _waitpid
+ _xpc_dictionary_get_value
- _CFAllocatorAllocate
- __ZN3abm12HelperServer6createENSt3__110shared_ptrIN3ctu9LogServerEEE
- __Znwm
CStrings:
+ " "
+ "%"
+ "%s"
+ "%s%u"
+ "%s: Child pid: %d, Encountered error while waiting. Error: %s"
+ "%s: Child pid: %d, Exited with status: %d, exitStatus: %d"
+ "%s: Child pid: %d, Failed setsid"
+ "%s: Child pid: %d, Failed to execv. Retval: %d, Error: %s"
+ "%s: Failed to fork. Error: %s"
+ "/usr/local/bin/setupOversteerLaunchpad.sh"
+ "/usr/sbin/arp -s "
+ "/usr/sbin/ndp -s "
+ "0 < argc && argc <= MAX_ARGC"
+ "169.254.0."
+ "Allowed"
+ "CarrierInstallCapability"
+ "CmdStruct"
+ "Command: %s"
+ "Couldn't find mac address for interface: %s"
+ "Desense"
+ "Interface"
+ "InternalBuild"
+ "Oversteer"
+ "ReleaseType"
+ "RootHelperServer.cpp"
+ "RootHelperServerCommandHandler"
+ "SetUltraConstrainedDefaultAllowed"
+ "SetupOversteer"
+ "SetupV4RouterForOversteer"
+ "SetupV6RouterForOversteer"
+ "Unable to get interface addresses for: %s"
+ "V6Router"
+ "Vendor"
+ "VendorNonUI"
+ "argWithPidIdx < argc"
+ "argc == count"
+ "basic_string"
+ "feth0"
+ "feth1"
+ "feth10"
+ "feth11"
+ "feth12"
+ "feth13"
+ "feth14"
+ "feth15"
+ "feth16"
+ "feth17"
+ "feth18"
+ "feth19"
+ "feth2"
+ "feth20"
+ "feth3"
+ "feth4"
+ "feth5"
+ "feth6"
+ "feth7"
+ "feth8"
+ "feth9"
+ "iface < kPeerOffset"
+ "net.link.generic.system.ultra_constrained_default_allowed"
+ "pdp_ip0"
+ "pdp_ip1"
+ "pdp_ip10"
+ "pdp_ip11"
+ "pdp_ip12"
+ "pdp_ip13"
+ "pdp_ip14"
+ "pdp_ip15"
+ "pdp_ip2"
+ "pdp_ip3"
+ "pdp_ip4"
+ "pdp_ip5"
+ "pdp_ip6"
+ "pdp_ip7"
+ "pdp_ip8"
+ "pdp_ip9"
+ "setupV4RouterForOversteer_sync"
+ "setupV6RouterForOversteer_sync"
+ "sysctlbyname failed: %s"
+ "sysctlbyname success: %s"
+ "v48@?0{ServerClientState={shared_ptr<TelephonyXPC::ServerClientState::State>=^{State}^{__shared_weak_count}}}8{dict={object=^v}}24{callback<void (^)(int, xpc::dict)>={block<void (^)(int, xpc::dict)>=@?}{queue={object=^{dispatch_object_s}}}}32"

```

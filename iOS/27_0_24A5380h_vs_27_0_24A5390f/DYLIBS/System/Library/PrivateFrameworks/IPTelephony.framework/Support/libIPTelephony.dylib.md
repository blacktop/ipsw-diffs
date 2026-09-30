## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2761.1.0.0.0
-  __TEXT.__text: 0x4aafb0
+2764.0.0.0.0
+  __TEXT.__text: 0x4ab92c
   __TEXT.__init_offsets: 0x1a4
-  __TEXT.__objc_methlist: 0x674
-  __TEXT.__const: 0x1f84c
-  __TEXT.__gcc_except_tab: 0x41e80
-  __TEXT.__cstring: 0x1410f
-  __TEXT.__oslogstring: 0x4cd41
-  __TEXT.__unwind_info: 0x18168
+  __TEXT.__objc_methlist: 0x74c
+  __TEXT.__const: 0x1f9fc
+  __TEXT.__gcc_except_tab: 0x41ec8
+  __TEXT.__cstring: 0x140b7
+  __TEXT.__oslogstring: 0x4cd37
+  __TEXT.__unwind_info: 0x181e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d98
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0x3d78
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x900
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x918
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x360e0
+  __AUTH_CONST.__const: 0x36308
   __AUTH_CONST.__cfstring: 0x2720
-  __AUTH_CONST.__objc_const: 0x9d0
+  __AUTH_CONST.__objc_const: 0xb80
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x16a0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x48
-  __DATA.__data: 0x268
+  __AUTH_CONST.__auth_got: 0x16b8
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__data: 0x2c8
   __DATA.__common: 0xa8
   __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 16405
-  Symbols:   25047
-  CStrings:  8705
+  Functions: 16438
+  Symbols:   25127
+  CStrings:  8702
 
Symbols:
+ -[NSPTokenFetcherImpl .cxx_destruct]
+ -[NSPTokenFetcherImpl auxiliaryAuthenticationCacheKey]
+ -[NSPTokenFetcherImpl fetchTokenAndAuxiliaryAuthenticationWithQueue:completionHandler:]
+ -[NSPTokenFetcherImpl generateTokenRequestWithQueue:completionHandler:]
+ -[NSPTokenFetcherImpl handleTokenResponse:withQueue:completionHandler:]
+ -[NSPTokenFetcherImpl initWithFetcher:]
+ -[NSPTokenFetcherImpl setAuxiliaryAuthenticationCacheKey:]
+ -[NSPTokenFetcherImpl setSystemClient:]
+ -[NSPTokenFetcherImpl systemClient]
+ _OBJC_CLASS_$_NSPTokenFetcherImpl
+ _OBJC_IVAR_$_NSPTokenFetcherImpl._fetcher
+ _OBJC_METACLASS_$_NSPTokenFetcherImpl
+ __OBJC_$_INSTANCE_METHODS_NSPTokenFetcherImpl
+ __OBJC_$_INSTANCE_VARIABLES_NSPTokenFetcherImpl
+ __OBJC_$_PROP_LIST_NSPTokenFetcherImpl
+ __OBJC_$_PROP_LIST_NSPTokenFetcherProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSPTokenFetcherProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSPTokenFetcherProtocol
+ __OBJC_$_PROTOCOL_REFS_NSPTokenFetcherProtocol
+ __OBJC_CLASS_PROTOCOLS_$_NSPTokenFetcherImpl
+ __OBJC_CLASS_RO_$_NSPTokenFetcherImpl
+ __OBJC_LABEL_PROTOCOL_$_NSPTokenFetcherProtocol
+ __OBJC_METACLASS_RO_$_NSPTokenFetcherImpl
+ __OBJC_PROTOCOL_$_NSPTokenFetcherProtocol
+ __ZN12_GLOBAL__N_115NSPProviderImpl22createAthmTokenFetcherEP6NSDataS2_
+ __ZN12_GLOBAL__N_115NSPProviderImpl23createAthmChallengeDataEv
+ __ZN12_GLOBAL__N_115NSPProviderImpl28saveAthmAuxiliaryAuthToCacheEP6NSDataP8NSStringS4_
+ __ZN12_GLOBAL__N_115NSPProviderImpl29createPatAndReputationFetcherEP6NSDataS2_S2_S2_P8NSString
+ __ZN12_GLOBAL__N_115NSPProviderImplD0Ev
+ __ZN12_GLOBAL__N_115NSPProviderImplD1Ev
+ __ZN12_GLOBAL__N_120NSPErrorInjectorImpl14errorForTargetERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_120NSPErrorInjectorImplD0Ev
+ __ZN12_GLOBAL__N_120NSPErrorInjectorImplD1Ev
+ __ZN12_GLOBAL__N_120NSPMetricsLoggerImpl21logPATRequestResponseERKN3ims9analytics25RCSPATRequestResponseInfoE
+ __ZN12_GLOBAL__N_120NSPMetricsLoggerImplD0Ev
+ __ZN12_GLOBAL__N_120NSPMetricsLoggerImplD1Ev
+ __ZN21NSPHelperDependenciesD2Ev
+ __ZN25NetworkServiceProxyHelper6createE12ClientConfig21NSPHelperDependencies
+ __ZNSt3__110unique_ptrIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_8NS_14default_deleteIS6_EEED1B9fqe220106Ev
+ __ZNSt3__110unique_ptrIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E4$_10NS_14default_deleteIS6_EEED1B9fqe220106Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEED1Ev
+ __ZTI11NSPProvider
+ __ZTI16NSPErrorInjector
+ __ZTI16NSPMetricsLogger
+ __ZTIN12_GLOBAL__N_115NSPProviderImplE
+ __ZTIN12_GLOBAL__N_120NSPErrorInjectorImplE
+ __ZTIN12_GLOBAL__N_120NSPMetricsLoggerImplE
+ __ZTINSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEEE
+ __ZTINSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEEE
+ __ZTINSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEEE
+ __ZTS11NSPProvider
+ __ZTS16NSPErrorInjector
+ __ZTS16NSPMetricsLogger
+ __ZTSN12_GLOBAL__N_115NSPProviderImplE
+ __ZTSN12_GLOBAL__N_120NSPErrorInjectorImplE
+ __ZTSN12_GLOBAL__N_120NSPMetricsLoggerImplE
+ __ZTSNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEEE
+ __ZTVN12_GLOBAL__N_115NSPProviderImplE
+ __ZTVN12_GLOBAL__N_120NSPErrorInjectorImplE
+ __ZTVN12_GLOBAL__N_120NSPMetricsLoggerImplE
+ __ZTVNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_115NSPProviderImplENS_9allocatorIS2_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPErrorInjectorImplENS_9allocatorIS2_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN12_GLOBAL__N_120NSPMetricsLoggerImplENS_9allocatorIS2_EEEE
+ __ZZN8dispatch5asyncIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_8EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ __ZZN8dispatch5asyncIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E4$_10EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$auxiliaryAuthenticationCacheKey
+ _objc_msgSend$initWithFetcher:
+ _objc_msgSend$systemClient
+ _objc_retain_x22
+ _objc_retain_x23
- __ZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl19checkErrorInjectionERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
- __ZN25NetworkServiceProxyHelper6createE12ClientConfig
- __ZNSt3__110unique_ptrIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_8NS_14default_deleteIS6_EEED1B9fqe220106Ev
- __ZZN8dispatch5asyncIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_8EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
CStrings:
+ "#E %{private, mask.hash}sBranded Calling header received : Invalid request"
+ "#I NSP error injection: injecting for target '%{public}s' (type '%{public}s')"
+ "%{private, mask.hash}sImsSocket %p : invalidating socket fd=%d"
+ "%{private, mask.hash}sImsSocket: detached from read source. cancel handler is now Closing fd %d"
+ "%{private, mask.hash}ssetTextMediaSessionMode: declining pending RTT upgrade for call %{private, mask.hash}s"
+ "nil PAT fetcher"
- "#D Using new API!"
- "#E %{private, mask.hash}sFailed to parse error type '%{public}s': %{public}s"
- "#E %{private, mask.hash}sNSP error injection enabled but no error type specified, using default (ServerFailure)"
- "#E %{private, mask.hash}sUnknown NSP error code %d for injection, using ServerFailure"
- "#I %{private, mask.hash}sNSP error injection: injecting error type '%{public}s' for target '%{public}s'"
- "%{private, mask.hash}s%s0x%lx%s%d"
- ": invalidating socket fd="
- "ImsSocket "
- "ImsSocket: detached from read source. cancel handler is now Closing fd "
```

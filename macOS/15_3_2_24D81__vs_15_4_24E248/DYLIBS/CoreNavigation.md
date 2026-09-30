## CoreNavigation

> `/System/Library/PrivateFrameworks/CoreNavigation.framework/Versions/A/CoreNavigation`

```diff

-343.0.2.0.0
-  __TEXT.__text: 0x2ff674
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__gcc_except_tab: 0x15024
-  __TEXT.__const: 0x3db8f
-  __TEXT.__cstring: 0x31a2a
+345.0.5.0.0
+  __TEXT.__text: 0x2fe35c
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__const: 0x4c5cf
+  __TEXT.__gcc_except_tab: 0x15014
+  __TEXT.__cstring: 0x3183a
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0xc9d0
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__unwind_info: 0xc4e8
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x8c8
-  __AUTH_CONST.__const: 0x1c400
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH_CONST.__const: 0x1c1a8
   __DATA.__data: 0x40
-  __DATA.__bss: 0x2098
-  __DATA.__common: 0x678
+  __DATA.__bss: 0x2158
+  __DATA.__common: 0x680
   __DATA_DIRTY.__common: 0x4b8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/Versions/A/Libraries/libprotobuf.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 5E29FF3C-ED69-310A-A038-DD988DDD9508
-  Functions: 13837
-  Symbols:   11469
-  CStrings:  3455
+  UUID: F169A1AA-AC26-3229-A8E1-AB5EDB607D21
+  Functions: 13579
+  Symbols:   11458
+  CStrings:  3442
 
Symbols:
+ __ZN11cnframework16ActiveObjectBase45HandleNextEventAndDetermineIfMoreWorkIsNeededEv
+ __ZN5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapper8InstanceEv
+ __ZNK5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapper26GetScaleFactorTableIndicesEfdRNSt3__14pairImmEE
+ __ZNK5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapper29GetUncertaintyScaleFactorCoreERKNS_18GNSSObservableTypeERKNS_8GnssBandERKNS_22RavenSignalEnvironmentERKNS_18RavenActivityStateERKNSt3__14pairImmEERKfNS0_30GNSSUncertaintyScaleFactorTypeE
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTIN5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapperE
+ __ZTINSt3__117bad_function_callE
+ __ZTSN5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapperE
+ __ZTVN5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapperE
+ __ZTVNSt3__117bad_function_callE
+ ___muldc3
+ _cblas_dgemm$NEWLAPACK
+ _dgecon$NEWLAPACK
+ _dgeevx$NEWLAPACK
+ _dgeqrf$NEWLAPACK
+ _dgesvd$NEWLAPACK
+ _dgetrf$NEWLAPACK
+ _dgetri$NEWLAPACK
+ _dormqr$NEWLAPACK
+ _dpotrf$NEWLAPACK
- __ZN11cnframework10Supervisor17SetThreadingModelERKNS_25CNFrameworkThreadingModelE
- __ZN11cnframework16ActiveObjectBase15HandleAllEventsEv
- __ZN11cnframework16ActiveObjectBase17SetThreadingModelERKNS_25CNFrameworkThreadingModelE
- __ZN11cnframework16ActiveObjectBase27HandleNextEventWithoutMutexEv
- __ZN11cnframework16ActiveObjectBaseD0Ev
- __ZN11cnframework16ActiveObjectBaseD1Ev
- __ZN11cnframework16ActiveObjectBaseD2Ev
- __ZNK11cnframework10Supervisor17GetThreadingModelEv
- __ZNK11cnframework16ActiveObjectBase17GetThreadingModelEv
- __ZNKSt9exception4whatEv
- __ZNSt3__115__thread_structC1Ev
- __ZNSt3__115__thread_structD1Ev
- __ZNSt3__118condition_variable10notify_allEv
- __ZNSt3__118condition_variable4waitERNS_11unique_lockINS_5mutexEEE
- __ZNSt3__118condition_variableD1Ev
- __ZNSt3__119__thread_local_dataEv
- __ZNSt3__120__throw_system_errorEiPKc
- __ZNSt3__15mutex8try_lockEv
- __ZNSt3__16thread4joinEv
- __ZNSt3__16threadD1Ev
- _cblas_dgemm
- _dgecon_
- _dgeevx_
- _dgeqrf_
- _dgesvd_
- _dgetrf_
- _dgetri_
- _dormqr_
- _dpotrf_
- _pthread_create
- _pthread_setspecific
CStrings:
+ "!boost::empty(rng)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPGnssMeasApi.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPGnssMsmtAnalysisToolData.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPInternalToolData.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPInternalToolDataTypes.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPPrivateDataCapture.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPPrivateDataShared.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRavenGnssAssistanceFile.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRavenLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRavenOutput.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRayTracingTileData.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRayTracingTilesAvailability.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPTropicalSavannaLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPVisionEvent.pb.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPVisionLogEntry.pb.cc"
+ "front"
- "#gmp,E1 mod value for PR unavailable"
- "#rxbc,Could not initialize receiver band correction LPF,sample_value,%.4f"
- "#rxbc,Could not initialize receiver band correction uncertainty LPF,sample_value,%.4f"
- "%s changing threading model from %u to %u"
- "%s thread not joinable"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPGnssMeasApi.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPGnssMsmtAnalysisToolData.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPInternalToolData.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPInternalToolDataTypes.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPPrivateDataCapture.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPPrivateDataShared.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRavenGnssAssistanceFile.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRavenLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRavenOutput.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRayTracingTileData.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPRayTracingTilesAvailability.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPTropicalSavannaLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPVisionEvent.pb.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreNavigation/shared/cnprotobuf/CoreNavigationCLPVisionLogEntry.pb.cc"
- "ConvertProtobufVIOInertialState, VIO Inertial State not present."
- "SetThreadingModel"
- "activeobjectbase.cpp"
- "cannot switch into MultiThreaded due to configuration"
- "false && \"cannot switch into MultiThreaded due to configuration\""
- "first != last"
- "point_to_range.hpp"
- "raven_threading_model"
- "supervisor.cpp"
- "thread constructor failed"

```

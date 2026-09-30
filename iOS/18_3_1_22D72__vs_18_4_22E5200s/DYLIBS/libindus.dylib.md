## libindus.dylib

> `/usr/lib/libindus.dylib`

```diff

-80.0.9.0.0
-  __TEXT.__text: 0x138a84
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__gcc_except_tab: 0x4ba8
-  __TEXT.__cstring: 0x252d9
-  __TEXT.__const: 0x4630
-  __TEXT.__unwind_info: 0x1d88
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x4d0
-  __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x1d08
+81.0.1.0.0
+  __TEXT.__text: 0x135af8
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__const: 0x4bd0
+  __TEXT.__gcc_except_tab: 0x4b98
+  __TEXT.__cstring: 0x25054
+  __TEXT.__oslogstring: 0xb
+  __TEXT.__unwind_info: 0x1c10
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x508
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_ptr: 0xa0
+  __AUTH_CONST.__const: 0x1cc8
   __AUTH_CONST.__cfstring: 0x40
   __AUTH.__data: 0x3f8
   __DATA.__data: 0x28620
-  __DATA.__common: 0x63fe1
   __DATA.__bss: 0x83f8
+  __DATA.__common: 0x63fe9
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1865
-  Symbols:   1962
-  CStrings:  3886
+  Functions: 1715
+  Symbols:   1956
+  CStrings:  3873
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __os_log_impl
+ _os_log_create
+ _os_log_type_enabled
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
CStrings:
+ "%{public}s"
+ "DD_BDS_IntEph_Valid:  FAILED:  SV %d  WeekNo = %d < %d, Too early !"
+ "DD_Proc_GPS_ION_UTC_Subframe:  Adopting OTA UTC Params, PRN %d"
+ "DD_Proc_GPS_ION_UTC_Subframe:  Ignoring OTA UTC Params, prefer source XOF, PRN %d"
+ "Feb 16 2025"
+ "ME_enc_o:  Illegal STE Constel ID "
+ "com.apple.gpsd"
+ "gpsdi"
+ "v2.38.0.2025-01-15"
- "%10u %s%c %s: #%04hx ConstType,%u\n"
- "%10u %s%c %s: #%04hx InitType\n"
- "%10u %s%c %s: #%04hx RevResp default, CPU,%c\n"
- "%10u %s%c %s: #%04hx Signal Band,%d\n"
- "%s FAILED: e = %g < %g, Unrealistic value!"
- "DD_Proc_GPS_Data"
- "GN_ABDS_Set_Alm: FAILED: e = %g < %g, Unrealistic value!"
- "GN_ABDS_Set_CNAV_Eph_El: FAILED: e = %g < %g, Unrealistic value!"
- "GN_AGAL_Set_Alm: FAILED: e = %g < %g, Unrealistic value!"
- "GN_AGAL_Set_Eph: FAILED: e = %g < %g, Unrealistic value!"
- "GN_AGPS_Set_Alm_El: FAILED: e = %g < %g, Unrealistic value!"
- "GN_ANVIC_Set_Alm_El: FAILED: e = %g < %g, Unrealistic value!"
- "GN_ANVIC_Set_Eph_El: FAILED: e = %g < %g, Unrealistic value!"
- "GN_EE_Get_BDS_CNAV_Eph_El: FAILED: e = %g < %g, Unrealistic value!"
- "GN_EE_Get_GAL_Eph_El:  FAILED:  e = %g  < %g, Unrealistic value !"
- "GN_EE_Get_NVIC_Eph_El: FAILED: e = %g < %g, Unrealistic value!"
- "Ga00_04HandleDeviceInit"
- "GncP24_51ConvertAGnssType"
- "Gncp24_56ConvertGnssType"
- "Jan 16 2025"
- "NK_Validate_Fix"
- "v2.37.2.2024-12-12"

```

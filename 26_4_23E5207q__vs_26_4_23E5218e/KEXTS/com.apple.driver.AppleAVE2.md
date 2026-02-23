## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-905.29.1.0.0
+905.36.1.0.0
   __TEXT.__const: 0x42610
-  __TEXT.__cstring: 0x40360
-  __TEXT.__os_log: 0x52151
-  __TEXT_EXEC.__text: 0x19b79c
+  __TEXT.__cstring: 0x4064b
+  __TEXT.__os_log: 0x5254f
+  __TEXT_EXEC.__text: 0x19c58c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0x130
   __DATA.__bss: 0x3f0
-  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x38

   __DATA_CONST.__const: 0x8b60
   __DATA_CONST.__kalloc_type: 0x4900
   __DATA_CONST.__kalloc_var: 0x2030
-  UUID: DCDDAD72-8EA1-3B96-B53D-3A38D69EA565
-  Functions: 2781
+  UUID: 838463EB-0235-37C5-B194-1E351219CA31
+  Functions: 2782
   Symbols:   0
-  CStrings:  8972
+  CStrings:  8986
 
CStrings:
+ "%lld %d AVE %s: %s:%d %s | invalid offset %p %d %lld %p %lld | 0x%llx %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | invalid offset %p %d %lld %p %lld | 0x%llx %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid slice count %p %lld %d %p %p %d"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid slice count %p %lld %d %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %lld %p %p %d %p "
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %lld %p %p %d %p \n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %p %d %lld"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %p %d %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %p %d %lld %lld %d %lld"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %p %d %lld %lld %d %lld\n"
+ "%lld %d AVE %s: FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d"
+ "%lld %d AVE %s: FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d\n"
+ "0 <= offset && offset < pInBuf->iSize && 0 <= size && offset + size <= pInBuf->iSize"
+ "0 <= offset && offset < pOutBuf->iSize && 0 <= size && offset + size <= pOutBuf->iSize"
+ "21112"
+ "21:50:37"
+ "905.36.1"
+ "AVE_ClientType_None <= type && type < AVE_ClientType_Max"
+ "AVE_EncType_HEVC == encType"
+ "AVE_EncType_None < encType && encType < AVE_EncType_Max"
+ "AVE_EncType_None == encType"
+ "Feb 17 2026"
+ "FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d"
+ "FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d\n"
+ "iSliceNum >= 0 && iSliceNum <= ((32) < (256) ? (32) : (256))"
+ "offset >= 0 && offset <= size && offset % 64 == 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iSize >= 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr % 64 ==0"
+ "pFrameInfo->PerFrameData.StillOffsetW % 64 == 0 && pFrameInfo->PerFrameData.StillOffsetH % 16 == 0 && offset >= 0 && offset <= size && offset % 64 == 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iSize > 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr % 64 ==0"
+ "pIODrv != nullptr && task != nullptr"
- "%lld %d AVE %s: %s:%d %s | invalid offset %p %d %lld %p %lld | 0x%llx %d %d"
- "%lld %d AVE %s: %s:%d %s | invalid offset %p %d %lld %p %lld | 0x%llx %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %p %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | wrong parameter %p %p %d %d\n"
- "%lld %d AVE %s: FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d"
- "%lld %d AVE %s: FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d\n"
- "2111"
- "23:51:17"
- "905.29.1"
- "Feb  4 2026"
- "FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d"
- "FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d\n"
- "offset %64 == 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iSize >= 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr % 64 ==0"
- "pFrameInfo->PerFrameData.StillOffsetW % 64 == 0 && pFrameInfo->PerFrameData.StillOffsetH % 16 == 0 && offset % 64 == 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iSize > 0 && pInfo->sInput.uInput.sLinear.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr % 64 ==0"

```

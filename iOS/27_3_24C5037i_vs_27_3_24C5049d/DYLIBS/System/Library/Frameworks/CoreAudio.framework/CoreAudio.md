## CoreAudio

> `/System/Library/Frameworks/CoreAudio.framework/CoreAudio`

```diff

-482.302.0.0.0
-  __TEXT.__text: 0x5388d4
-  __TEXT.__realtime: 0x28a78
+482.303.0.0.0
+  __TEXT.__text: 0x5388c0
+  __TEXT.__realtime: 0x28a7c
   __TEXT.__delay_stubs: 0x780
   __TEXT.__delay_helper: 0x148
   __TEXT.__objc_methlist: 0x17c4
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ __ZN26HALS_IOContext_Legacy_Impl29Server_Internal_StartIOProcIDEPFijPK14AudioTimeStampPK15AudioBufferListS2_PS3_S2_PvEPS0_j : 4008 -> 4004
~ __ZN26HALS_IOContext_Legacy_Impl28Server_Internal_StopIOProcIDEPFijPK14AudioTimeStampPK15AudioBufferListS2_PS3_S2_PvE : 1592 -> 1588
~ __ZN26HALS_IOContext_Legacy_Impl7PauseIOEj : 780 -> 776
~ __ZN26HALS_IOContext_Legacy_Impl8ResumeIOEj : 1224 -> 1220
~ __ZN26HALS_IOContext_Legacy_Impl39ExecuteWorkWithControlAndIOThreadLockerEN5caulk12function_refIFvvEEE : 208 -> 204
~ __ZN14HALS_IOEngine222_WriteToStream_MixableEjP25HALS_IOEngine2_StreamInfojRK17HALS_IOEngineInfoRK15HALS_BufferInfo : 920 -> 924
```

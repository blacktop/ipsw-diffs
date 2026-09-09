## libglInterpose.dylib

> `/usr/lib/libglInterpose.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 310.8.0.0.0
-  __TEXT.__text: 0x1ea79c
+  __TEXT.__text: 0x1ea774
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0xee0
   __TEXT.__init_offsets: 0x4
Functions:
~ __Z31has_client_memory_vertex_arraysP11ContextInfo : 624 -> 628
~ __Z22copyout_vertex_arrays2P11ContextInfolllb : 3816 -> 3820
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE6resizeEm : 284 -> 288
~ __ZN16ContextHarvester20harvestBufferObjectsEv : 496 -> 492
~ __ZN16ContextHarvester15harvestSamplersEv : 188 -> 184
~ __ZN16ContextHarvester20harvestRenderbuffersEv : 192 -> 188
~ __ZN16ContextHarvester18harvestSyncObjectsEv : 188 -> 184
~ __ZN16ContextHarvester24harvestLegacyARBProgramsEv : 180 -> 176
~ __ZN16ContextHarvester19harvestFramebuffersEv : 188 -> 184
~ __ZN16ContextHarvester19harvestQueryObjectsEv : 200 -> 196
~ __ZN16ContextHarvester27harvestGLSLProgramPipelinesEv : 188 -> 184
~ __ZN16ContextHarvester35harvestGLSLPrograms_LinkedStatePassEv : 188 -> 184
~ __ZN16ContextHarvester36harvestGLSLPrograms_CurrentStatePassEv : 188 -> 184
~ __ZN16ContextHarvester18harvestGLSLShadersEv : 368 -> 364
~ __ZN16ContextHarvester23harvestGLSLShaderLabelsEv : 196 -> 192
~ __ZN16ContextHarvester23encodeGLSLShaderDeletesEv : 564 -> 560
~ _OUTLINED_FUNCTION_10 -> _OUTLINED_FUNCTION_9 : 16 -> 28
~ _OUTLINED_FUNCTION_11 : 20 -> 16
~ _OUTLINED_FUNCTION_12 : 16 -> 20
~ _OUTLINED_FUNCTION_14 : 28 -> 16
```

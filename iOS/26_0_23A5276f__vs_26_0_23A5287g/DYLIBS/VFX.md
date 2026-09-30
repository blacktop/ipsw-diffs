## VFX

> `/System/Library/PrivateFrameworks/VFX.framework/VFX`

```diff

-203.0.17.0.5
-  __TEXT.__text: 0xd11600
+203.0.21.0.0
+  __TEXT.__text: 0xd25e48
   __TEXT.__auth_stubs: 0x6d60
-  __TEXT.__objc_methlist: 0x1d684
-  __TEXT.__const: 0x8d128
-  __TEXT.__gcc_except_tab: 0x6854
-  __TEXT.__oslogstring: 0x11bc4
-  __TEXT.__cstring: 0xbb741
+  __TEXT.__objc_methlist: 0x1d6bc
+  __TEXT.__const: 0x8d428
+  __TEXT.__gcc_except_tab: 0x6888
+  __TEXT.__cstring: 0xbba87
+  __TEXT.__oslogstring: 0x11b7e
   __TEXT.__ustring: 0x22
-  __TEXT.__swift5_typeref: 0xddd8
-  __TEXT.__swift5_fieldmd: 0x1d4e4
-  __TEXT.__constg_swiftt: 0x278dc
-  __TEXT.__swift5_reflstr: 0x1362d
-  __TEXT.__swift5_builtin: 0x1338
-  __TEXT.__swift5_mpenum: 0x27c
-  __TEXT.__swift5_assocty: 0x3aa8
+  __TEXT.__constg_swiftt: 0x27a1c
+  __TEXT.__swift5_typeref: 0xdcde
+  __TEXT.__swift5_fieldmd: 0x1d6d0
+  __TEXT.__swift5_builtin: 0x13d8
+  __TEXT.__swift5_reflstr: 0x13764
+  __TEXT.__swift5_assocty: 0x3ac0
+  __TEXT.__swift5_proto: 0x6f14
+  __TEXT.__swift5_types: 0x24c0
   __TEXT.__swift5_capture: 0x11648
+  __TEXT.__swift5_mpenum: 0x27c
   __TEXT.__swift5_protos: 0x1f4
-  __TEXT.__swift5_proto: 0x6f04
-  __TEXT.__swift5_types: 0x249c
-  __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift5_types2: 0x8
+  __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x78
-  __TEXT.__unwind_info: 0x27dc8
-  __TEXT.__eh_frame: 0x2dae4
+  __TEXT.__unwind_info: 0x280c8
+  __TEXT.__eh_frame: 0x2dab0
   __TEXT.__objc_classname: 0x210d
-  __TEXT.__objc_methname: 0x2c7a4
-  __TEXT.__objc_methtype: 0x15963
-  __TEXT.__objc_stubs: 0x20e00
-  __DATA_CONST.__got: 0x1e60
-  __DATA_CONST.__const: 0x7128
+  __TEXT.__objc_methname: 0x2c81c
+  __TEXT.__objc_methtype: 0x158b4
+  __TEXT.__objc_stubs: 0x20e20
+  __DATA_CONST.__got: 0x1e58
+  __DATA_CONST.__const: 0x7158
   __DATA_CONST.__objc_classlist: 0x1fe0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x600
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbdb0
+  __DATA_CONST.__objc_selrefs: 0xbdc0
   __DATA_CONST.__objc_protorefs: 0x380
   __DATA_CONST.__objc_superrefs: 0x660
   __DATA_CONST.__objc_arraydata: 0x368
   __AUTH_CONST.__auth_got: 0x36c8
-  __AUTH_CONST.__const: 0x8c538
-  __AUTH_CONST.__cfstring: 0x194a0
-  __AUTH_CONST.__objc_const: 0x47f00
+  __AUTH_CONST.__const: 0x8c8a0
+  __AUTH_CONST.__cfstring: 0x194c0
+  __AUTH_CONST.__objc_const: 0x47f70
   __AUTH_CONST.__objc_intobj: 0x570
-  __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0xc468
-  __AUTH.__data: 0x365b8
+  __AUTH.__data: 0x36570
   __AUTH.__thread_vars: 0x90
   __AUTH.__thread_data: 0x8
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x1d28
-  __DATA.__data: 0x1373c
-  __DATA.__bss: 0x7bdd0
-  __DATA.__common: 0xf81
+  __DATA.__objc_ivar: 0x1d30
+  __DATA.__data: 0x13ac8
+  __DATA.__bss: 0x7c010
+  __DATA.__common: 0xf89
   __DATA_DIRTY.__objc_data: 0x3fb0
-  __DATA_DIRTY.__data: 0x10e30
+  __DATA_DIRTY.__data: 0x10e50
   __DATA_DIRTY.__bss: 0xbbe9
   __DATA_DIRTY.__common: 0x618
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FABD3F9E-CEAC-3763-8F66-1A3D38E9F7FB
-  Functions: 66042
-  Symbols:   2596
-  CStrings:  24905
+  UUID: FE7F91A3-B3BD-3EF5-9947-BD66B7B2A18B
+  Functions: 65782
+  Symbols:   2597
+  CStrings:  24915
 
Symbols:
+ _swift_cvw_initializeBufferWithCopyOfBuffer
CStrings:
+ "#ifndef __VFX_RENDER_OPTIONS_H__\n#define __VFX_RENDER_OPTIONS_H__\n\n#ifndef VFX_ENUM \n#define VFX_ENUM(type) enum __attribute__((enum_extensibility(closed))) : type\n#endif\n\ntypedef VFX_ENUM(uint16_t) {\n    vfx_render_option_enable_clipping                                        = (0x1 << 0),\n    vfx_render_option_enable_breakthrough                                    = (0x1 << 1),\n    vfx_render_option_enable_dither_fade                                     = (0x1 << 2),\n    vfx_render_option_enable_nearfield_vignetting                            = (0x1 << 3),\n    vfx_render_option_enable_portal_clipping                                 = (0x1 << 4),\n    vfx_render_option_enable_depth_mitigation                                = (0x1 << 5),\n    vfx_render_option_render_for_blur                                        = (0x1 << 6),\n    vfx_render_option_enable_spatial_focus                                   = (0x1 << 7),\n    vfx_render_option_enable_visual_depth_static_occlusion                   = (0x1 << 8),\n    vfx_render_option_enable_scene_understanding_static_occlusion            = (0x1 << 9),\n    vfx_render_option_enable_visual_depth_static_occlusion_texture_available = (0x1 << 10),\n} vfx_render_options;\n\nstatic inline uint16_t renderOptionsEnableClipping(uint16_t flags) {\n    return flags | vfx_render_option_enable_clipping;\n}\n\nstatic inline uint16_t renderOptionsEnableBreakthrough(uint16_t flags) {\n    return flags | vfx_render_option_enable_breakthrough;\n}\n\nstatic inline uint16_t renderOptionsEnableDitherFade(uint16_t flags) {\n    return flags | vfx_render_option_enable_dither_fade;\n}\n\nstatic inline uint16_t renderOptionsEnableNearfieldVignetting(uint16_t flags) {\n    return flags | vfx_render_option_enable_nearfield_vignetting;\n}\n\nstatic inline uint16_t renderOptionsEnablePortalClipping(uint16_t flags) {\n    return flags | vfx_render_option_enable_portal_clipping;\n}\n\nstatic inline uint16_t renderOptionsEnableDepthMitigation(uint16_t flags) {\n    return flags | vfx_render_option_enable_depth_mitigation;\n}\n\nstatic inline uint16_t renderOptionsRenderForBlur(uint16_t flags) {\n    return flags | vfx_render_option_render_for_blur;\n}\n\nstatic inline uint16_t renderOptionsEnableSpatialFocus(uint16_t flags) {\n    return flags | vfx_render_option_enable_spatial_focus;\n}\n\nstatic inline uint16_t renderOptionsEnableVisualDepthStaticOcclusion(uint16_t flags) {\n    return flags | vfx_render_option_enable_visual_depth_static_occlusion;\n}\n\nstatic inline uint16_t renderOptionsEnableSceneUnderstandingStaticOcclusion(uint16_t flags) {\n    return flags | vfx_render_option_enable_scene_understanding_static_occlusion;\n}\n\nstatic inline uint16_t renderOptionsEnableVisualDepthStaticOcclusionTextureAvailable(uint16_t flags) {\n    return flags | vfx_render_option_enable_visual_depth_static_occlusion_texture_available;\n}\n\nstatic inline bool renderOptionsIsClippingEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_clipping) != 0;\n}\n\nstatic inline bool renderOptionsIsBreakthroughEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_breakthrough) != 0;\n}\n\nstatic inline bool renderOptionsIsNearfieldVignettingEnabled(uint16_t flags) {\n    return false;\n    return (flags & vfx_render_option_enable_nearfield_vignetting) != 0;\n}\n\nstatic inline bool renderOptionsIsDitherFadeEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_dither_fade) != 0;\n}\n\nstatic inline bool renderOptionsPortalClipPlaneEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_portal_clipping) != 0;\n}\n\nstatic inline bool renderOptionsIsDepthMitigationEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_depth_mitigation) != 0;\n}\n\nstatic inline bool renderOptionsIsSpatialFocusEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_spatial_focus) != 0;\n}\n\nstatic inline bool renderOptionsIsRenderingForBlur(uint16_t flags) {\n    return (flags & vfx_render_option_render_for_blur) != 0;\n}\n\nstatic inline bool renderOptionsIsVisualDepthStaticOcclusionEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_visual_depth_static_occlusion) != 0;\n}\n\nstatic inline bool renderOptionsIsSceneUnderstandingStaticOcclusionEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_scene_understanding_static_occlusion) != 0;\n}\n\nstatic inline bool renderOptionsIsVisualDepthStaticOcclusionTextureAvailableEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_visual_depth_static_occlusion_texture_available) != 0;\n}\n\n#ifdef __cplusplus\nstruct render_options_override {\n    uint16_t overrideBits = 0;\n    uint16_t overrideValues = 0;\n\n    void disableClipping() {\n        disable(vfx_render_option_enable_clipping);\n    }\n\n    void disableDitherFade() {\n        disable(vfx_render_option_enable_dither_fade);\n    }\n\n    void enableDitherFade() {\n        enable(vfx_render_option_enable_dither_fade);\n    }\n\n    void disableBreakthrough() {\n        disable(vfx_render_option_enable_breakthrough);\n    }\n\n    void enableNearFieldVignetting() {\n        enable(vfx_render_option_enable_nearfield_vignetting);\n    }\n\n    uint16_t applyOverrideOn(uint16_t optionFlags) const {\n        return (optionFlags | (overrideValues & overrideBits)) & (overrideValues | ~overrideBits);\n    }\n\n    void enable(uint16_t flag) {\n        overrideBits |= flag;\n        overrideValues |= flag;\n    }\n\n    void disable(uint16_t flag) {\n        overrideBits |= flag;\n        overrideValues &= ~flag;\n    }\n};\n#endif\n\n#endif \n"
+ "Enable Handtracking"
+ "EnableDepthMitigation"
+ "EnableNearFieldVignetting"
+ "EnableRuntimeFunctionConstants"
+ "EnableSceneUnderstandingStaticOcclusion"
+ "EnableSpatialFocus"
+ "EnableVisualDepthStaticOcclusion"
+ "TB,N,V_isHandTrackingEnabled"
+ "Welcome to VFX 203.0.21 (Jun 28 2025 03:04:30)"
+ "_isHandTrackingEnabled"
+ "_isHandTrackingScriptPresent"
+ "_updateActiveTriggerTypesWithMoveNeeded:"
+ "isHandTrackingEnabled"
+ "isPresentation"
+ "parentTransaction == self"
+ "setHandTrackingEnabled:"
+ "setIsHandTrackingEnabled:"
- "#ifndef __VFX_RENDER_OPTIONS_H__\n#define __VFX_RENDER_OPTIONS_H__\n\n#ifndef VFX_ENUM \n#define VFX_ENUM(type) enum __attribute__((enum_extensibility(closed))) : type\n#endif\n\ntypedef VFX_ENUM(uint16_t) {\n    vfx_render_option_enable_clipping                             = (0x1 << 0),\n    vfx_render_option_enable_breakthrough                         = (0x1 << 1),\n    vfx_render_option_enable_dither_fade                          = (0x1 << 2),\n    vfx_render_option_enable_nearfield_vignetting                 = (0x1 << 3),\n    vfx_render_option_enable_portal_clipping                      = (0x1 << 4),\n    vfx_render_option_enable_depth_mitigation                     = (0x1 << 5),\n    vfx_render_option_render_for_blur                             = (0x1 << 6),\n    vfx_render_option_enable_spatial_focus                        = (0x1 << 7),\n    vfx_render_option_enable_visual_depth_static_occlusion        = (0x1 << 8),\n    vfx_render_option_enable_scene_understanding_static_occlusion = (0x1 << 9),\n} vfx_render_options;\n\nstatic inline uint16_t renderOptionsEnableClipping(uint16_t flags) {\n    return flags | vfx_render_option_enable_clipping;\n}\n\nstatic inline uint16_t renderOptionsEnableBreakthrough(uint16_t flags) {\n    return flags | vfx_render_option_enable_breakthrough;\n}\n\nstatic inline uint16_t renderOptionsEnableDitherFade(uint16_t flags) {\n    return flags | vfx_render_option_enable_dither_fade;\n}\n\nstatic inline uint16_t renderOptionsEnableNearfieldVignetting(uint16_t flags) {\n    return flags | vfx_render_option_enable_nearfield_vignetting;\n}\n\nstatic inline uint16_t renderOptionsEnablePortalClipping(uint16_t flags) {\n    return flags | vfx_render_option_enable_portal_clipping;\n}\n\nstatic inline uint16_t renderOptionsEnableDepthMitigation(uint16_t flags) {\n    return flags | vfx_render_option_enable_depth_mitigation;\n}\n\nstatic inline uint16_t renderOptionsRenderForBlur(uint16_t flags) {\n    return flags | vfx_render_option_render_for_blur;\n}\n\nstatic inline uint16_t renderOptionsEnableSpatialFocus(uint16_t flags) {\n    return flags | vfx_render_option_enable_spatial_focus;\n}\n\nstatic inline uint16_t renderOptionsEnableVisualDepthStaticOcclusion(uint16_t flags) {\n    return flags | vfx_render_option_enable_visual_depth_static_occlusion;\n}\n\nstatic inline uint16_t renderOptionsEnableSceneUnderstandingStaticOcclusion(uint16_t flags) {\n    return flags | vfx_render_option_enable_scene_understanding_static_occlusion;\n}\n\nstatic inline bool renderOptionsIsClippingEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_clipping) != 0;\n}\n\nstatic inline bool renderOptionsIsBreakthroughEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_breakthrough) != 0;\n}\n\nstatic inline bool renderOptionsIsNearfieldVignettingEnabled(uint16_t flags) {\n    return false;\n    return (flags & vfx_render_option_enable_nearfield_vignetting) != 0;\n}\n\nstatic inline bool renderOptionsIsDitherFadeEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_dither_fade) != 0;\n}\n\nstatic inline bool renderOptionsPortalClipPlaneEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_portal_clipping) != 0;\n}\n\nstatic inline bool renderOptionsIsDepthMitigationEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_depth_mitigation) != 0;\n}\n\nstatic inline bool renderOptionsIsSpatialFocusEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_spatial_focus) != 0;\n}\n\nstatic inline bool renderOptionsIsRenderingForBlur(uint16_t flags) {\n    return (flags & vfx_render_option_render_for_blur) != 0;\n}\n\nstatic inline bool renderOptionsIsVisualDepthStaticOcclusionEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_visual_depth_static_occlusion) != 0;\n}\n\nstatic inline bool renderOptionsIsSceneUnderstandingStaticOcclusionEnabled(uint16_t flags) {\n    return (flags & vfx_render_option_enable_scene_understanding_static_occlusion) != 0;\n}\n\n#ifdef __cplusplus\nstruct render_options_override {\n    uint16_t overrideBits = 0;\n    uint16_t overrideValues = 0;\n\n    void disableClipping() {\n        disable(vfx_render_option_enable_clipping);\n    }\n\n    void disableDitherFade() {\n        disable(vfx_render_option_enable_dither_fade);\n    }\n\n    void enableDitherFade() {\n        enable(vfx_render_option_enable_dither_fade);\n    }\n\n    void disableBreakthrough() {\n        disable(vfx_render_option_enable_breakthrough);\n    }\n\n    void enableNearFieldVignetting() {\n        enable(vfx_render_option_enable_nearfield_vignetting);\n    }\n\n    uint16_t applyOverrideOn(uint16_t optionFlags) const {\n        return (optionFlags | (overrideValues & overrideBits)) & (overrideValues | ~overrideBits);\n    }\n\n    void enable(uint16_t flag) {\n        overrideBits |= flag;\n        overrideValues |= flag;\n    }\n\n    void disable(uint16_t flag) {\n        overrideBits |= flag;\n        overrideValues &= ~flag;\n    }\n};\n#endif\n\n#endif \n"
- "-[VFXWorld triggerManager]"
- "@24@0:8^{__CFXCoreEntityHandle={__CFXEntity={__CFRuntimeBase=QAQ}^v^{__CFString}^{__CFString}^{__CFDictionary}^{__CFXWorld}q}^{__CFString}^{__CFDictionary}^{__CFArray}iB^v}16"
- "Assertion '%s' failed. invalid renderer"
- "Error: can't copy a presentation core entity handle"
- "Welcome to VFX 203.0.17.0.5 (Jun 14 2025 09:18:09)"
- "_installViewport"
- "initWithCoreEntityHandleRef:"
- "isDuplicating"
- "presentationHandleWithCFXCoreEntityHandle:"

```

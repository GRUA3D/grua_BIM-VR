using UnrealBuildTool;

public class GRUA_IMP3DEditorTarget : TargetRules
{
	public GRUA_IMP3DEditorTarget(TargetInfo Target) : base(Target)
	{
		DefaultBuildSettings = BuildSettingsVersion.V3;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		Type = TargetType.Editor;
		ExtraModuleNames.Add("GRUA_IMP3D");
	}
}

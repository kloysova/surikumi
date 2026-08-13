my $project_texinputs = $ENV{'TEXINPUTS'} || '';
my $project_tfmfonts = $ENV{'TFMFONTS'} || '';
my $project_t1fonts = $ENV{'T1FONTS'} || '';
my $project_afmfonts = $ENV{'AFMFONTS'} || '';
my $project_fontmaps = $ENV{'TEXFONTMAPS'} || '';

$ENV{'TEXINPUTS'} = './texmf/tex//:' . $project_texinputs;
$ENV{'TFMFONTS'} = './texmf/fonts/tfm//:' . $project_tfmfonts;
$ENV{'T1FONTS'} = './texmf/fonts/type1//:' . $project_t1fonts;
$ENV{'AFMFONTS'} = './texmf/fonts/afm//:' . $project_afmfonts;
$ENV{'TEXFONTMAPS'} = './texmf/fonts/map//:' . $project_fontmaps;

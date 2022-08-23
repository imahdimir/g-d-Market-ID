##

"""

  """

##

from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import read_data_according_to_type as rdata


ufm_repo_url = 'https://github.com/imahdimir/d-uniq-Final-Markets'
cur_module_repo = 'https://github.com/imahdimir/gov-d-uniq-Final-Markets'

mktid = 'MarketId'
name = 'Name'

def main() :


  pass

  ##
  ufm = GithubData(ufm_repo_url)
  ufm.clone()
  ##
  fpn = ufm.data_filepath
  ##
  df = rdata(fpn)
  ##
  df = df[[mktid, name]]
  ##
  df = df.applymap(norm)
  ##
  df = df.sort_values([mktid, name])
  ##
  df = df.drop_duplicates()
  ##
  sxl(df , fpn)
  ##
  commit_msg = 'sorted'
  commit_msg += f' by repo: {cur_module_repo}'

  ufm.commit_push(commit_msg)
  ##
  ufm.rmdir()

  ##

##